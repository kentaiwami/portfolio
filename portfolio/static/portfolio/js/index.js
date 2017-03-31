function isScrolledIntoView(elem) {
    var docViewTop = $(window).scrollTop();
    var docViewBottom = docViewTop + $(window).height();

    var elemTop = $(elem).offset().top;
    var elemBottom = elemTop + $(elem).height();

    return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
}

function click_submit() {
	$('#submit_btn').hide();

	var console_center_message_div = $('<div>');
	console_center_message_div.html('Now Submitting');
	console_center_message_div.addClass('console_center_message');

	$('#submitting_message_area').append(console_center_message_div);
}