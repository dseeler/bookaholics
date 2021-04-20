let appliedPromo = false;

window.onload = (event) => {
    if ($("#user-state").val() !== 'None') {
        $("#state").val($("#user-state").val());
    }

    // Add shipping fee to total
    $("#total").html((parseFloat($("#total").html()) + 5.99).toFixed(2));

    // Add tax to total
    calculateTax();

    // Update total value
    const total = (parseFloat($("#total").html()) + parseFloat($("#tax").html())).toFixed(2);
    $("#total-input").val(total);

    document.getElementById("redeem-button").onclick = (event) => {
        event.preventDefault();
        redeemCode();
    }
}

function redeemCode(){
    if (appliedPromo){
        $("#promo-error").html("Can't apply another promotion");
        return;
    }

    const promo_code = $("#promo_code").val().toUpperCase();

    // Required for Django POST request
    const csrftoken = Cookies.get('csrftoken');

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    // AJAX request
    $.ajax({
        headers: {
            "X-CSRFToken": csrftoken
        },
        url: "/redeem_promo",
        type: 'POST',
        data: {
            'promo_code': JSON.stringify(promo_code),
        },
        dataType: 'json',
        success:
            function (response) {
                if (response[0].toString().includes("Invalid") || response[0].toString().includes("expired") || 
                response[0].toString().includes("starts")){
                    $("#promo-error").html(response[0]);
                }
                else{
                    $("#promo-code-block").addClass("text-success");
                    $("#promo-code-id").html(promo_code + " - " + response[0] + "% off");
                    const discount = (parseFloat($("#total").html()) * parseFloat("." + response[0])).toFixed(2);
                    $("#promo-code-discount").html("-$" + discount);
                    $("#total").html((parseFloat($("#total").html()) - discount).toFixed(2));
                    calculateTax();
                    appliedPromo = true;
                    $("#promo-input").val(promo_code);
                }
            },
        error:
            function () {
                console.log("Failed");
            }
    });
}

function clearPromoError(){
    $("#promo-error").html("");
}

function calculateTax(){
    const tax = (parseFloat($("#total").html()) * .04);
    $("#tax").html(tax.toFixed(2));
    $("#total").html((parseFloat($("#total").html()) + tax).toFixed(2));
    $("#total-input").val((parseFloat($("#total").html()) + tax).toFixed(2));
}