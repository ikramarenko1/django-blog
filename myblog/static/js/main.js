// 
// ======  LIKE POST  ======
// 
$('#toggle_like').on('click', function(e) {
	e.preventDefault();
	var likeButton = $(this);
	var post_id = likeButton.data('post-id');

	var csrftoken = getCookie('csrftoken');
	
	$.ajax({
		url: likeButton.data('like-url'),
		type: 'POST',
		data: {'csrfmiddlewaretoken': csrftoken},
		dataType: 'json',
		success: function(data) {
			if (data.liked) {
				likeButton.addClass('active');
			} else {
				likeButton.removeClass('active');
			}
			$('#like_count').text(data.like_count);
		},
		error: function(xhr, status, error) {
			console.error(xhr.responseText);
		}
	});
});

// Для получения csrftoken
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// 
// ======  COMMENT  ======
// 
const textareas = document.querySelectorAll('textarea');

textareas.forEach(textarea => {
	const parentContainer = textarea.closest('div');
	const submitButton = parentContainer.querySelector('input[type="submit"]');

	submitButton.disabled = true;
	
	textarea.addEventListener('input', function () {
		this.style.height = 'auto';
		this.style.height = this.scrollHeight + 'px';

		if (this.value.trim() === '') {
			submitButton.disabled = true;
		} else {
			submitButton.disabled = false;
		}
	});
});
