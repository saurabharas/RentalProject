<?php
$con = mysqli_connect('localhost','sau','Sau#651994');
$con2=mysqli_select_db ($con,'ajaxtestdb');
if (!$con || !$con2) {
    die('Could not connect: ' . mysqli_error($con));
}
#print("connectted")

$sql=" SELECT * FROM `checkboxtable` ";
$result = mysqli_query($con,$sql);
while($row = mysqli_fetch_array($result, MYSQLI_NUM))
{
   
		 echo "id:".$row[0]." name: ".$row[1]."<br>";
		 
} 


?>