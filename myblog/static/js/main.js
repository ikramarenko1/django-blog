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
