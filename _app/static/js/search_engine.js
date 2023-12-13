$(document).ready(function(){
	$('#char-search').keyup(function(){
		var search = $(this).val();
		$('.char').each(function(){
			var text = $(this).find('h1').find("a").text();
			if(search == '' || text.toLowerCase().indexOf(search) != -1 || text.toLowerCase() == search){
				$(this).show();
			}else{
				$(this).hide();
			}
		});
	});

	$(".char").click(function(){
		var id = $(this).attr('id');
		window.location.href = "/func/" + id;
	});
});