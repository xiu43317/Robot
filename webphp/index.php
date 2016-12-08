<html><head>
    <meta name=viewport content="user-scalable=0">
    <meta http-equiv="refresh" content="5">
    <style type="text/css">
body{
    width:100%;
    font-family:sans-serif;
    margin:0;
    padding:0;
    text-align:center;
}
.left{
    text-align:left;
}
.img{
    display: inline-block;
    margin: 1em;x
}
button{
    background-color:#EFEFEF;
    border-radius:4px;
    border:1px solid #D0D0D0;
    overflow:auto;
    width:40%;
/*  padding:2px 8px;*/
    text-align:center;
    padding:3px 0px;
    cursor:pointer;
/*  opacity:0.5;*/
}
button:hover {
    background:white;
}
    </style>
    <script src=https://code.jquery.com/jquery-1.12.1.min.js></script>
    <script>
function resize(){
    w = $('body').width();
    h = $('body').height();
    f = h / 20 > w / 20 ? w / 20 : h / 20;
    $('button').css('font-size', f);
}
$().ready(function(){
    resize();
    $(window).resize(resize);
});
    </script>
</head><body>
    <h1>網路監控相簿</h1>
    <div class=left>
<?php 
        $files = glob("./uploads/*.*");
        for ($i=0; $i<count($files); $i++)
        {
            $j = $i + 1;
            $num = $files[$i]; 
            echo    '<div class="img">'.
                        '<p>image'.$j.'</p>'.
                        '<a target="_blank" href="./'.$num.'"><img src="./'.$num.'" width="200" height="150"></a>'.
                    '</div>';
        }           


?>
    </div><br><button type=button onclick="window.history.back();">Return</button>
</body></html>

