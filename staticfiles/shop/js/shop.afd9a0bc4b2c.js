$(document).ready(function () {
    $('.productValue').click(function (event) {
        event.preventDefault();
        var productId = $(this).attr('id');
        console.log(productId);

        $.ajax({
            url: '{% url "shop: add_to_cart" %}',
            url: '{% url "like-post" %}',
            type: 'POST',
            data: {
                'product_id': $('#' + productId).val(),
                'csrfmiddlewaretoken': "{{ csrf_token }}",
                'action': 'post'
            },
            success: function (response) {
                console.log("success");
            },
            error: function (rs, e) {
                console.log(e.response)
            }
        })
    })
})