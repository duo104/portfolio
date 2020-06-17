<?php

$db = new PDO('mysql:dbname=php;host=localhost;charset=utf8','root','root');

if(isset($_POST['submit'])){
  $content = $_POST['content_name'];

  $sql = "insert into doing (content) values ('$content')";
  $insert = $db->query($sql);
}

$sql = 'select content from doing';
$results = $db->query($sql);

 ?>

<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <title>ToDoリスト</title>
  </head>
  <body>
    <h1>ToDoリスト</h1>
    <form class="" action="index.php" method="post">
      <ul>
        <li><span>タスク名 </span><input type="text" name="content_name" value="">
        <span><input type="submit" name="submit"></span></li>
      </ul>
    </form>
    <ul>
      <?php

        foreach($results as $result){
          echo '<li>';
          echo $result['content'];
          echo '</li>';
        }

       ?>
    </ul>
  </body>
</html>
