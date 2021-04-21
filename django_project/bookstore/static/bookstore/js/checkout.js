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

    document.getElementById("order-button").onclick = (event) => {
        event.preventDefault();
        // Add validation function
    }
}

function validateAll(){
    if(validateName() && validateAddress() && validateCard()){
        $("#checkout-form").submit();
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

function validateName(){
    let valid = true;

    if ($("#first_name").val().length < 1){
        $("#first_name").attr("style", "border: 1px solid red");
        $("#first-name-error").html("Can't be empty!");
        valid = false;
    }

    if ($("#last_name").val().length < 1){
        $("#last_name").attr("style", "border: 1px solid red");
        $("#last-name-error").html("Can't be empty!");
        valid = false;
    }

    if ($("#first_name").val().length > 20){
        $("#first_name").attr("style", "border: 1px solid red");
        $("#first-name-error").html("Must be <=20 characters");
        valid = false;
    }

    if ($("#last_name").val().length > 20){
        $("#last_name").attr("style", "border: 1px solid red");
        $("#last-name-error").html("Must be <=20 characters");
        valid = false;
    }

    return valid;
}


function clearFirstName(){
    $("#first_name").attr("style", "border: 1px solid black");
    $("#first-name-error").html("");
}


function clearLastName(){
    $("#last_name").attr("style", "border: 1px solid black");
    $("#last-name-error").html("");
}


function validateAddress(){
    let valid = true;

    if ($("#street").val().length < 1){
        $("#street").attr("style", "border: 1px solid red");
        $("#street-error").html("Can't be empty");
        valid = false;
    }

    if ($("#city").val().length < 1){
        $("#city").attr("style", "border: 1px solid red");
        $("#city-error").html("Can't be empty");
        valid = false;
    }

    if ($("#state").val().length != 2){
        $("#state").attr("style", "border: 1px solid red");
        $("#state-error").html("Must be an abbreviation");
        valid = false;
    }

    if ($("#zip_code").val().length != 5){
        $("#zip_code").attr("style", "border: 1px solid red");
        $("#zip-code-error").html("Must be 5 characters");
        valid = false;
    }

    if (/[^a-zA-Z]/.test($("#city").val())){
        $("#city").attr("style", "border: 1px solid red");
        $("#city-error").html("Only letters allowed");
        valid = false;
    }


    if (/[^a-zA-Z]/.test($("#state").val())){
        $("#state").attr("style", "border: 1px solid red");
        $("#state-error").html("Only letters allowed");
        valid = false;
    }

    if (/\D/.test($("#zip_code").val())){
        $("#zip_code").attr("style", "border: 1px solid red");
        $("#zip-code-error").html("Only digits allowed");
        valid = false;
    }

    return valid;
}

function clearStreet(){
    $("#street").attr("style", "border: 1px solid black");
    $("#street-error").html("");
}

function clearCity(){
    $("#city").attr("style", "border: 1px solid black");
    $("#city-error").html("");
}

function clearState(){
    $("#state").attr("style", "border: 1px solid black");
    $("#state-error").html("");
}

function clearZipCode(){
    $("#zip_code").attr("style", "border: 1px solid black");
    $("#zip-code-error").html("");
}


function validateCard(){
    let valid = true;

    if ($("#card_num").val().length != 16){
        $("#card_num").attr("style", "border: 1px solid red");
        $("#card-num-error").html("Must be 16 characters");
        valid = false;
    }

    if ($("#card_exp").val().length != 5){
        $("#card_exp").attr("style", "border: 1px solid red");
        $("#card-exp-error").html("Must be in MM/YY format");
        valid = false;
    }

    if ($("#card_code").val().length != 3){
        $("#card_code").attr("style", "border: 1px solid red");
        $("#card-code-error").html("Must be 3 characters");
        valid = false;
    }

    if (/\D/.test($("#card_num").val())){
        $("#card_num").attr("style", "border: 1px solid red");
        $("#card-num-error").html("Only digits allowed");
        valid = false;
    }

    if (/\D/.test($("#card_code").val())){
        $("#card_code").attr("style", "border: 1px solid red");
        $("#card-code-error").html("Only digits allowed");
        valid = false;
    }

    return valid;
}

function clearCardNum(){
    $("#card_num").attr("style", "border: 1px solid black");
    $("#card-num-error").html("");
}


function clearCardExp(){
    $("#card_exp").attr("style", "border: 1px solid black");
    $("#card-exp-error").html("");
}

function clearCardCode(){
    $("#card_code").attr("style", "border: 1px solid black");
    $("#card-code-error").html("");
}
