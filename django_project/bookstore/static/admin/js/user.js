window.onload = (event) => {
    $("#id_password").html("<div style='font-size: 5px'>&nbsp</div><span>Encrypted</span>");
    $(".help").hide();

    // Hide card_code
    $("#id_card_name").val("Encrypted");
    $("#id_card_name").attr("disabled", "true");
    $("#id_card_name").attr("style", "background-color: white; border: none");

    // Hide card_num
    $("#id_card_num").val("Encrypted");
    $("#id_card_num").attr("disabled", "true");
    $("#id_card_num").attr("style", "background-color: white; border: none");

    // Hide card_exp
    $("#id_card_exp").val("Encrypted");
    $("#id_card_exp").attr("disabled", "true");
    $("#id_card_exp").attr("style", "background-color: white; border: none");

    // Hide card_code
    $("#id_card_code").val("Encrypted");
    $("#id_card_code").attr("disabled", "true");
    $("#id_card_code").attr("style", "background-color: white; border: none");
}

