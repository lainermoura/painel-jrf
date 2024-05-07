// Evento para colar link de reunião e carregar conteúdo abaixo (do iframe)
parent.document.querySelector('iframe[data-testid="stIFrame"]').parentElement.style.display = 'none';

document.addEventListener('DOMContentLoaded', function() {
    
    const targetElement = parent.document.querySelector('iframe[title="st_keyup.st_keyup"]').contentDocument.getElementById('input_box');

    let intervalId = setInterval(() => {
        console.log('dsdsd');
        if (targetElement !== null) {
            clearInterval(intervalId);
            console.log('Elemento visível!');
            targetElement.addEventListener('paste', handlePaste);

            function handlePaste(event) {
                const clipboardData = event.clipboardData || top.window.clipboardData;
                const pastedData = clipboardData.getData('text');
                console.log({pastedData});
                event.preventDefault();

                targetElement.value = pastedData;
                targetElement.dispatchEvent(new Event('keyup'));
            }
        }
        clearInterval(intervalId);
    }, 100);
}, false);