$(document).ready(function(){
	$(window).scroll(function(){
		if($(window).scrollTop()>300){
			$('.my_bttn').fadeIn(250);
		}
		else{
			$('.my_bttn').fadeOut(250);
		}
	});
	$('.my_bttn').click(function(){
		$('html,body').animate(
			{scrollTop:0},400
			);
	});
});


{/* <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<link rel="stylesheet" href="topbutton.css">
<script src="topbutton.js"></script> */}