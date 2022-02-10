$(function () {
    // toggle show cart
    $(".cart").on("click", function () {
        console.log('kkk');
        $(".shopping-cart").toggleClass("d-none");
    });
    hideCartOnClickAway('.shopping-cart')

    //order page
    updateValues()
    $('#size,#topping,#quantity').on('change', function(){
        updateValues()
    })

})

calculateTotal = () => {
    const pizzaPrice = +$('#size option:selected').data('price')
    const toppingsPrice = +$('#topping option:selected').data('price') || 0
    const qty = +$('#quantity').val() || 1
    return (pizzaPrice+toppingsPrice) * qty
}

updateValues = () => {
    if (!!$('#topping').val()) {
        $('.topping').text($('#topping option:selected').text())
    }
    if(!!$('#quantity').val()){
        $('.quantity').text($('#quantity').val())
    }
    
    $('.total').text(calculateTotal())
}


function hideCartOnClickAway(selector) {
    $(document).on('mouseup', function (e) {
        var container = $(selector);

        // if the target of the click isn't the container nor a descendant of the container
        if (!container.is(e.target) && container.has(e.target).length === 0 && container.css('display') != 'none') {
            container.addClass("d-none")
        }
    });
}