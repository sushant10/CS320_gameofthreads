$(document).ready(function(){
    $(".nav-tabs a").click(function(){
        $(this).tab('show');
    });
	$(".nav-tabs a").first().click();
});