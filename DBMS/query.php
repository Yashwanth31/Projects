<?php 
	include ('dbco.php');
	$regisid=$rloc=$rph='';
	if(isset($_POST['submit1'])){
		$regisid=$_POST['regid'];
		$rloc=$_POST['loc'];
		$rph=$_POST['oph'];
		$q1="INSERT into registration values($regisid,$loc,$oph)";
		$result1=mysqli_query($connect,$q1);
	}
?>
