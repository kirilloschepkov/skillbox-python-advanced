document.addEventListener('DOMContentLoaded', () => {
    setInterval(updateTime, 1000)
    function updateTime() {
        const time = new Date()
        document.querySelector('.container').innerHTML = `${time.getHours()}:${time.getMinutes()}:${time.getSeconds()}`
    }
})