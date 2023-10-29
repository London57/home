$(function ($) {
    $('.btn btn-primary').submit(function(e){
        $.ajax({
            type:this.method,
            url:this.action,
            data: $(this).serialize(),
            success: function(response) {
                console.log('ok - ', response)
            },
            error: function(response) {
                console.log('error - ', response)
            }
        })
    })
})