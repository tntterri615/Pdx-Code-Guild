function card_value(card) {
        if (card === 'jack' || card === 'queen' || card === 'q' || card === 'king' || card === 'k'){
            return 10;
        }
        else if ( card === 'ace' || card === 'a'){
            return 1;
        }
        else {
            return parseInt(card);
        }
    }

document.querySelector('#run').onclick = function() {
    let card1 = document.querySelector('#card1');
    let card2 = document.querySelector('#card2');
    let card3 = document.querySelector('#card3');

    let first_card = card1.value;                  // can combine this section with the one below it; kept separate for clarity
    let second_card = card2.value;
    let third_card = card3.value;

    let first_value = card_value(first_card);
    let second_value = card_value(second_card);
    let third_value = card_value(third_card);

    let card_total = first_value + second_value + third_value;

    if (card_total <= 11) {
        if (first_card === 'ace' || second_card === 'ace' || third_card === 'ace' || first_card === 'a' || second_card === 'a' || third_card === 'a') {
            card_total += 10;
        }
    }
    let div = document.querySelector('#hand_value');
    div.innerText = card_total;

    if (card_total < 17){
        div.innerText = card_total + ', Hit';
    }
    else if (card_total >= 17 && card_total <= 21){
        div.innerText = card_total + ', Stay'
    }
    else if (card_total > 21) {
        div.innerText = card_total + ', Busted'
    }
};