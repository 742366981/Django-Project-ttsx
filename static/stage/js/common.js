function getCartCount() {
            $.get('/contents/getPrice/',function (data) {
                 $('#show_count').text(data.counts);
            });
        }
getCartCount();