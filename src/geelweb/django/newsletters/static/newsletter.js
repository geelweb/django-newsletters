var newsletter = {
    add: function(field) {
        var email = $(field).val();
        $.ajax('/newsletter/subscribe/', {
            'data': {'email': email}
        }).done(function(data) {
            if (data['code'] == 200) {
                $('.newsletter_message').html('<p class="text-success">' + data['message'] + '</p>')
            } else {
                $('.newsletter_message').html('<p class="text-danger">' + data['message'] + '</p>')
            }
        });
    }
}
