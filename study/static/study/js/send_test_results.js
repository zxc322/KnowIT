$(function ($) {

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $('#save_test_results').submit(function (e) {
        e.preventDefault()
        const data = {};
        data['test_id'] = $('input[name = "test-id"]').val()
        let questions_elements = $('.test-question')
        questions_elements.each(function (el) {
            let question = $( this ).text()
            data[question] = $(`input[name = "${question}"]:checked`).val()
        })
        console.log("data:", data)

        $.ajax({
            type: this.method,
            url: this.action,
            data: data,
            headers: {'X-CSRFToken': getCookie('csrftoken')},
            dataType: 'json',
            success: function (response) {
                console.log('ok - ', response)
                },

            error: function (response) {
                console.log('err - ', response)
            }
        })
    })
})