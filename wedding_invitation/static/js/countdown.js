document.addEventListener('DOMContentLoaded', () => {
    const countdown = document.querySelector('[data-countdown]');

    if (!countdown) {
        return;
    }

    const targetDate = new Date(countdown.dataset.countdown).getTime();
    const days = countdown.querySelector('[data-days]');
    const hours = countdown.querySelector('[data-hours]');
    const minutes = countdown.querySelector('[data-minutes]');
    const seconds = countdown.querySelector('[data-seconds]');

    const pad = (value) => String(value).padStart(2, '0');

    const updateCountdown = () => {
        const distance = Math.max(targetDate - Date.now(), 0);

        const dayValue = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hourValue = Math.floor((distance / (1000 * 60 * 60)) % 24);
        const minuteValue = Math.floor((distance / (1000 * 60)) % 60);
        const secondValue = Math.floor((distance / 1000) % 60);

        days.textContent = pad(dayValue);
        hours.textContent = pad(hourValue);
        minutes.textContent = pad(minuteValue);
        seconds.textContent = pad(secondValue);
    };

    updateCountdown();
    setInterval(updateCountdown, 1000);
});
