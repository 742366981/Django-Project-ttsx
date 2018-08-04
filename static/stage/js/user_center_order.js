function noPrice(id) {
    $.ajax({
        url:'/contents/oPrice/',
        data:{'o_id':id},
        success:function (data) {
            if(data.code=='200'){
                $('#no'+id).text(data.prices+'元');
            }
        }
    });
}


function yesPrice(id) {
    $.ajax({
        url:'/contents/oPrice/',
        data:{'o_id':id},
        success:function (data) {
            if(data.code=='200'){
                $('#yes'+id).text(data.prices+'元');
            }
        }
    });
}