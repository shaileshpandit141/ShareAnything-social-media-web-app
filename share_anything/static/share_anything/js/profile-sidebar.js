const userProfileBtn = document.getElementById('userProfileBtn')
const crossBtn = document.getElementById('crossBtn')
const sideBar = document.getElementById('sideBar')

sideBar.setAttribute('data-btnState', '1')

function hendelSideBarClick(btn, btnState) {
    btn.addEventListener('click', (event) => {
        event.preventDefault()
        
        if (sideBar.getAttribute('data-btnState') === '1') {
            sideBar.setAttribute('data-btnState', '0')
            sideBar.style.transform= 'translateX(0)'
            console.log('if');
        } else {
            sideBar.setAttribute('data-btnState', '1')
            sideBar.style.transform= 'translateX(300px)'
        }
    })
}

hendelSideBarClick(userProfileBtn)
hendelSideBarClick(crossBtn)
