function addCart(id) {
            var csrf = $('input[name="csrfmiddlewaretoken"]').val()
            $.ajax({
                type:'POST',
                url:'/contents/addCart/',
                headers:{'X-CSRFToken': csrf},
                dataType:'json',
                data:{'g_id':id},
                success:function (data) {
                    if (data.code == '200') {
                        $('.num' + id).val(data.c_num);
                        getPrice();
                    }
                }
            });
        }