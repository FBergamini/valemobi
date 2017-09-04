<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<html>
  <head>
    <title>Plataforma de Transações</title>
    <link rel="stylesheet" href="styles.css">
    <script>
      // Função para retornar à página anterior
      function voltar() {
          window.history.back();
      }
    </script>
  </head>
  <body>
    <h1>Nova transação</h1>
    <?php
      // Cria variaveis mais curtas para cada valor recebido
      $cod=$_POST['cod'];
      $tipoMerc=$_POST['tipoMerc'];
      $nome=$_POST['nome'];
      $quant=$_POST['quant'];
      $preco=$_POST['preco'];
      $tipoNeg=$_POST['tipoNeg'];

      // Prepara o texto para poder ser armazenado no banco de dados
      if (!get_magic_quotes_gpc()) {
        $cod = addslashes($cod);
        $tipoMerc = addslashes($tipoMerc);
        $nome= addslashes($nome);
        $quant= addslashes($quant);
        $preco= addslashes($preco);
        $tipoNeg= addslashes($tipoNeg);
      }

      // Faz a conexão com o banco de dados
      @ $db = new mysqli('mysql.hostinger.com.br', 'u556965789_root', 'password', 'u556965789_valem');

      // Caso não consiga conectar, retorna um erro ao usuário
      if (mysqli_connect_errno()) {
         echo "<p style='text-align: center;'>Erro: Falha ao conectar ao banco de dados.</p>";
         exit;
      }

      // Executa o comando SQL para inserir a transação no banco de dados
      $query = "insert into valemobi (cod, tipoMerc, nome, quant, preco, tipoNeg) values
                ('".$cod."', '".$tipoMerc."', '".$nome."', '".$quant."', '".$preco."', '".$tipoNeg."')";
      $result = $db->query($query);

      // Avisa o usuário do sucesso ou falha da inserção da transação
      if ($result) {
          echo "<p style='text-align: center;'>Transação inserida no banco de dados.</p>";
      } else {
              echo "<p style='text-align: center;'>Occoreu algum erro. A transação não foi inserida.</p>";
      }

      // Termina a conexão com o banco de dados
      $db->close();
    ?>
    <br><button class="centerButton" onclick="voltar()">Voltar</button>
  </body>
</html>