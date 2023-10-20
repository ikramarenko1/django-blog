// 
// ======  LIKE POST  ======
// 
$(document).ready(function() {
	let csrftoken = getCookie('csrftoken');
	let post_id = $('#toggle_like').data('post-id');

	$.ajax({
        url: '/check_like_status/',
        type: 'POST',
        data: {'post_id': post_id, 'csrfmiddlewaretoken': csrftoken},
        dataType: 'json',
        success: function(data) {
            if (data.liked) {
                $('#toggle_like').addClass('active');
            }
            $('#like_count').text(data.like_count);
        },
        error: function(xhr, status, error) {
            console.error(xhr.responseText);
        }
    });

	$('#toggle_like').on('click', function(e) {
		e.preventDefault();
		let likeButton = $(this);
		let post_id = likeButton.data('post-id');
		
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
});

// Для получения csrftoken
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i]);
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
$('textarea').each(function() {
	const textarea = $(this);
	const parentContainer = textarea.closest('div');
	const submitButton = parentContainer.find('input[type="submit"]');

	submitButton.prop('disabled', true);

	textarea.on('input', function() {
		this.style.height = 'auto';
		this.style.height = this.scrollHeight + 'px';

		if ($(this).val().trim() === '') {
			submitButton.prop('disabled', true);
		} else {
			submitButton.prop('disabled', false);
		}
	});
});
