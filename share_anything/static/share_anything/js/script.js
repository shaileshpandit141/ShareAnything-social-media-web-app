const optionBtnsEl = document.querySelectorAll('.option--btn')
const optionBtnIconEl = document.querySelectorAll('.option--btn--icon')
const optionsEls = document.querySelectorAll('.options--cont')

// || For Comment Action
const commentBtnsEl = document.querySelectorAll('.comment--btn')
const CommentComponents = document.querySelectorAll('.comment--component')


let optionState = true

function handelOptionBtnClick() {

    for (let index = 0; index < optionBtnsEl.length; index++) {

        optionBtnsEl[index].addEventListener('click', (event) => {
            event.preventDefault()
            if (optionState) {
                optionState = !optionState
                optionsEls[index].style.opacity = 1
                optionsEls[index].style.height = '140px'
                optionBtnIconEl[index].style.transform = 'rotate(0deg)'
            } else {
                optionState = !optionState
                optionsEls[index].style.opacity = 1
                optionsEls[index].style.height = '0'
                optionBtnIconEl[index].style.transform = 'rotate(-180deg)'
            }
        })

    }

}
handelOptionBtnClick()

let btnState = true

function handelCommentBtnClick() {

    for (let index = 0; index < commentBtnsEl.length; index++) {

        commentBtnsEl[index].addEventListener('click', (event) => {
            event.preventDefault()

            if (btnState) {
                btnState = !btnState
                CommentComponents[index].style.height = '50px'
            } else {
                btnState = !btnState
                CommentComponents[index].style.height = '0px'
            }
        })
    }
}
handelCommentBtnClick()