const display = $('#display-chars');
const all_chars = display.children();

$().ready(function() {
	let childs = display.children();
	$('#char-search').keyup(function() {
		var query;
		query = $(this).val();
		childs.each(function() {
			var child;
			child = $(this);
			if (child.text().toLowerCase().indexOf(query.toLowerCase()) === -1) {
				child.hide();
			} else {
				child.show();
			}
		});
	});
});