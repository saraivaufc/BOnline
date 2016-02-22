/* Register */
function showKey(){
	$("input[name='key']").removeAttr("disabled");
	$("label[for='id_key']").css({'display': 'block'});
	$("input[name='key']").css({'display': 'block'});
	$("input[name='key']").attr("required","required");
}
function hideKey(){
	$("input[name='key']").removeAttr("required");
	$("input[name='key']").attr("disabled", "disabled");
	$("label[for='id_key']").css({'display': 'none'});
	$("input[name='key']").css({'display': 'none'});
}
$("select[name='group']").change(function(){
	if($(this).val() != "generalUser"){
		showKey();
	}else{
		hideKey();
	}
});