<?php
//DADOS PARA RELATÓRIO EM PDF
$dados = "<!DOCTYPE html>";
$dados .= "<html>";
$dados .= "<head>";
$dados .= "<meta charset='UTF-8'>";
$dados .= "<title>OmniCare - Receitas da Consulta</title>";
$dados .= "<style>
body { font-family: Arial, sans-serif; color: #2C3E50; }
h1 { color: #0D7377; font-size: 24px; margin-bottom: 8px; }
h2 { color: #14919B; font-size: 16px; margin-top: 0; }
table { width: 100%; border-collapse: collapse; margin-top: 14px; }
th { background-color: #0D7377; color: white; padding: 8px; border: 1px solid #B8D4E3; font-size: 12px; }
td { padding: 8px; border: 1px solid #B8D4E3; font-size: 11px; }
tr:nth-child(even) { background-color: #F5FAFA; }
.rodape { margin-top: 16px; font-size: 11px; color: #555; }
</style>";
$dados .= "</head>";
$dados .= "<body>";

include('ligarBD.php'); //incluir ligação à BD
date_default_timezone_set('Europe/Lisbon'); //definir timezone para Portugal

$idConsulta = isset($_GET['id_consulta']) ? intval($_GET['id_consulta']) : 0;

$dados .= "<h1>OmniCare - Relatório de Receitas</h1>";
$dados .= "<h2>Consulta #" . $idConsulta . "</h2>";

if ($idConsulta <= 0) {
    $dados .= "<p>ID de consulta inválido.</p>";
} else {
    //Query para obter registos de receitas/medicamentos da consulta
    $sql = "SELECT r.Id AS IdReceita,
                   m.Nome AS Medicamento,
                   COALESCE(rm.Observacoes, '') AS Observacoes,
                   DATE_FORMAT(rm.DataInicio, '%d/%m/%Y') AS DataInicio,
                   CASE WHEN rm.DataFim IS NULL THEN '' ELSE DATE_FORMAT(rm.DataFim, '%d/%m/%Y') END AS DataFim
            FROM receitas r
            JOIN receitas_medicamentos rm ON r.Id = rm.IdReceita
            JOIN medicamentos m ON rm.IdMedicamento = m.Id
            WHERE r.IdConsulta = :idConsulta
            ORDER BY r.Id, rm.DataInicio DESC";

    $result_sql = $conn->prepare($sql); //preparar a query
    $result_sql->bindValue(':idConsulta', $idConsulta, PDO::PARAM_INT);
    $result_sql->execute(); //executar a query

    $dados .= "<table>";
    $dados .= "<tr><th>Receita</th><th>Medicamento</th><th>Observações</th><th>Data Início</th><th>Data Fim</th></tr>";

    $totalRegistos = 0;
    while($row_sql = $result_sql->fetch(PDO::FETCH_ASSOC)) { //Ler os registos devolvidos pela execução da query
        $totalRegistos++;
        $dados .= "<tr>";
        $dados .= "<td>" . htmlspecialchars($row_sql['IdReceita']) . "</td>";
        $dados .= "<td>" . htmlspecialchars($row_sql['Medicamento']) . "</td>";
        $dados .= "<td>" . htmlspecialchars($row_sql['Observacoes']) . "</td>";
        $dados .= "<td>" . htmlspecialchars($row_sql['DataInicio']) . "</td>";
        $dados .= "<td>" . htmlspecialchars($row_sql['DataFim']) . "</td>";
        $dados .= "</tr>";
    }

    if ($totalRegistos === 0) {
        $dados .= "<tr><td colspan='5'>Sem registos para esta consulta.</td></tr>";
    }

    $dados .= "</table>";
}

$dados .= "<p class='rodape'>Relatório gerado a " . date('d/m/Y H:i') . "</p>";
$dados .= "</body></html>";

//GERAR PDF
if (!file_exists('dompdf/autoload.inc.php')) {
    die('Erro: pasta dompdf não encontrada. Coloca a pasta dompdf dentro do projeto.');
}

require_once 'dompdf/autoload.inc.php'; //carregar a classe Dompdf
$dompdf = new \Dompdf\Dompdf(); //instanciar a class dompdf
$dompdf->loadHtml($dados); //instanciar dados HTML e enviar conteúdo do pdf
$dompdf->setPaper('A4', 'portrait'); //configurar o tamanho e orientação do papel
$dompdf->render(); //renderizar no html com pdf
$dompdf->stream("receitas_consulta_" . $idConsulta . ".pdf", array('Attachment' => false)); //gerar o PDF
?>