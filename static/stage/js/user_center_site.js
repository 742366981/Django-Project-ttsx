function removeAddress(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        type:'POST',
        url:'/contents/removeAddress/',
        data:{'id':id},
        dataType:'json',
        headers:{'X-CSRFToken': csrf},
        success:function (data) {
            if(data.code=='200'){
                $('#remove'+id).parent().remove()
            }
        }
    });
}