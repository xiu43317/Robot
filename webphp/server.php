<?php
$target_path = "uploads/";
//$target_path = $target_path . basename( $_FILES['image1']['name']); 
$explode_filename = explode (".", $_FILES['image1']['name']);
$upload_filename = date("Ymd-His") . "." . $explode_filename[1];
if(move_uploaded_file($_FILES['image1']['tmp_name'],$target_path.$upload_filename)) {
    echo "1";
}
print_r($_FILES);
?>