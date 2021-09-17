<?php
$con=mysqli_connect("localhost","root","","waterlevel");// server, user, password, database
if (mysqli_connect_errno())
{
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$result = mysqli_query($con,"SELECT ID, wLevel, date FROM level WHERE ID=(SELECT MAX(ID) FROM level)");

echo "<table border='1'>
<tr>
<th>Current ID</th>
<th>Water Level</th>
<th>Date</th>
</tr>";

while($row = mysqli_fetch_array($result)){
    echo "<tr>";
    echo "<td>" . $row['ID'] . "</td>";
    $value=$row['wLevel'];
    echo "<td>" . $row['wLevel'] . "</td>";
    echo "<td>" . $row['date'] . "</td>";
}
echo "</table>";
if($value>=5&&$value<9){
    echo "<img src='assets/cup50.png'>";
}
else if($value>=9){
    echo "<img src='assets/cup100.png'>";
}
else{
    echo "<img src='assets/cup0.png'>";
}
mysqli_close($con);
?>