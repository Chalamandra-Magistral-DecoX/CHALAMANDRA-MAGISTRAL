// ELEMENTOS DOM - Cacheado para mejor performance
const DOM = {
    form: document.getElementById('oracle-form'),
    method: document.getElementById('method'),
    context: document.getElementById('context'),
    situation: document.getElementById('situation'),
    resultSection: document.getElementById('result-section'),
    questionsOutput: document.getElementById('questions-output'),
    ctaSection: document.getElementById('cta-section'),
    emailCta: document.getElementById('email-cta'),
    subscribeCta: document.getElementById('subscribe-cta'),
    emailForm: document.getElementById('email-form'),
    userEmail: document.getElementById('user-email')
};

// UTILIDADES
const utils = {
    show(element) {
        element.classList.remove('hidden');
    },

    hide(element) {
        element.classList.add('hidden');
    },

    validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    },

    personalizeQuestion(question, context) {
        return question.replace(/\[contexto\]/g, context);
    },

    scrollToElement(element) {
        element.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
};

// GENERADOR DE PREGUNTAS
const questionGenerator = {
    generate(method, context, situation) {
        const methodData = QUESTION_BANK[method];
        if (!methodData) {
            throw new Error('Método no encontrado');
        }

        let outputHTML = '';

        // Generar HTML para cada categoría de preguntas
        Object.entries(methodData).forEach(([category, questions]) => {
            outputHTML += this.createQuestionBlock(category, questions, situation, method);
        });

        return outputHTML;
    },

    createQuestionBlock(category, questions, situation, method) {
        const isSixHats = method === "6 Sombreros";
        const color = isSixHats ? HAT_COLORS[category] : null;

        return `
            <div class="questions-block">
                <div class="hat-title">
                    ${color ? `<span class="hat-color" style="background-color: ${color};"></span>` : ''}
                    <span>${category}</span>
                </div>
                <ul class="questions-list">
                    ${questions.map(question =>
                        `<li>${utils.personalizeQuestion(question, situation)}</li>`
                    ).join('')}
                </ul>
            </div>
        `;
    }
};

// MANEJADORES DE EVENTOS
const eventHandlers = {
    handleFormSubmit(e) {
        e.preventDefault();

        const method = DOM.method.value;
        const context = DOM.context.value;
        const situation = DOM.situation.value;

        if (!method || !context || !situation) {
            alert('Por favor, completa todos los campos');
            return;
        }

        try {
            const questionsHTML = questionGenerator.generate(method, context, situation);
            DOM.questionsOutput.innerHTML = questionsHTML;

            utils.show(DOM.resultSection);
            utils.show(DOM.ctaSection);

            utils.scrollToElement(DOM.resultSection);

            // Tracking (simulado)

        } catch (error) {
            alert('Error al generar las preguntas. Intenta nuevamente.');
        }
    },

    handleEmailCta() {
        utils.show(DOM.emailForm);
        DOM.userEmail.focus();
    },

    handleSubscribeCta() {
        window.open('https://chalamandra.substack.com', '_blank');
    },

    handleEmailSubmit(e) {
        e.preventDefault();

        const email = DOM.userEmail.value.trim();

        if (!utils.validateEmail(email)) {
            alert('Por favor, introduce un email válido');
            return;
        }

        // Simular envío de email
        alert(`¡Resultados enviados a ${email}! Revisa tu bandeja de entrada.`);
        utils.hide(DOM.emailForm);
        DOM.userEmail.value = '';

        // Simular tag en CRM
    }
};

// INICIALIZACIÓN
function init() {
    // Event Listeners
    DOM.form.addEventListener('submit', eventHandlers.handleFormSubmit);
    DOM.emailCta.addEventListener('click', eventHandlers.handleEmailCta);
    DOM.subscribeCta.addEventListener('click', eventHandlers.handleSubscribeCta);
    DOM.emailForm.addEventListener('submit', eventHandlers.handleEmailSubmit);
}

// Iniciar aplicación cuando el DOM esté listo
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}
