from flask import Blueprint, request, jsonify
import json
import random

chatbot_bp = Blueprint('chatbot', __name__)

# Base de conocimiento del agente IA
knowledge_base = {
    "servicios": {
        "agentes_ia": {
            "descripcion": "Desarrollamos asistentes virtuales inteligentes que automatizan procesos y mejoran la experiencia de tus clientes.",
            "beneficios": [
                "Atención al cliente 24/7 sin interrupciones",
                "Automatización de procesos repetitivos",
                "Análisis de datos y generación de insights",
                "Personalización basada en comportamiento del usuario",
                "Integración con sistemas existentes"
            ],
            "paquetes": {
                "starter": {
                    "nombre": "Agente IA Starter",
                    "descripcion": "Ideal para pequeñas empresas que buscan automatizar tareas sencillas",
                    "caracteristicas": [
                        "Diseño y desarrollo de un agente IA conversacional básico",
                        "Integración en una plataforma",
                        "Hasta 5 intenciones y 20 frases de ejemplo",
                        "Soporte técnico básico por 1 mes",
                        "Documentación de uso"
                    ]
                },
                "pro": {
                    "nombre": "Agente IA Pro",
                    "descripcion": "Solución completa para empresas que necesitan un agente IA más robusto",
                    "caracteristicas": [
                        "Agente IA avanzado con múltiples intenciones",
                        "Integración en hasta 2 plataformas",
                        "Hasta 15 intenciones y 50 frases de ejemplo",
                        "Personalización de respuestas y tono de voz",
                        "Análisis de métricas y reportes básicos",
                        "Soporte técnico prioritario por 3 meses"
                    ]
                },
                "empresarial": {
                    "nombre": "Agente IA Empresarial",
                    "descripcion": "La solución definitiva para grandes empresas",
                    "caracteristicas": [
                        "Agente IA altamente complejo y escalable",
                        "Integración en múltiples plataformas y sistemas",
                        "Capacitación ilimitada con intenciones personalizadas",
                        "Procesamiento de Lenguaje Natural avanzado",
                        "Análisis de sentimientos y personalización dinámica",
                        "Soporte técnico 24/7 por 6 meses"
                    ]
                }
            }
        },
        "apps_moviles": {
            "descripcion": "Diseñamos y desarrollamos apps nativas e híbridas con experiencias de usuario excepcionales.",
            "beneficios": [
                "Diseño UX/UI intuitivo y atractivo",
                "Desarrollo para iOS y Android",
                "Integración con APIs y servicios externos",
                "Mantenimiento y actualizaciones continuas"
            ],
            "paquetes": {
                "esencial": {
                    "nombre": "App Móvil Esencial",
                    "descripcion": "Perfecto para emprendedores o pequeñas empresas",
                    "caracteristicas": [
                        "Aplicación móvil nativa o híbrida",
                        "Hasta 5 pantallas principales",
                        "Funcionalidades básicas",
                        "Publicación en una tienda de aplicaciones",
                        "Soporte técnico básico por 1 mes"
                    ]
                },
                "avanzada": {
                    "nombre": "App Móvil Avanzada",
                    "descripcion": "Ideal para empresas que buscan funcionalidades interactivas",
                    "caracteristicas": [
                        "Aplicación móvil para iOS y Android",
                        "Hasta 10 pantallas principales",
                        "Funcionalidades avanzadas y notificaciones push",
                        "Integración con API externa",
                        "Publicación en ambas tiendas",
                        "Soporte técnico prioritario por 3 meses"
                    ]
                },
                "empresarial": {
                    "nombre": "App Móvil Empresarial",
                    "descripcion": "Solución integral para empresas que requieren aplicaciones complejas",
                    "caracteristicas": [
                        "Aplicación móvil nativa con arquitectura escalable",
                        "Número ilimitado de pantallas",
                        "Integración con múltiples APIs y sistemas",
                        "Funcionalidades avanzadas como geolocalización",
                        "Optimización de rendimiento y seguridad",
                        "Soporte técnico 24/7 por 6 meses"
                    ]
                }
            }
        },
        "paginas_web": {
            "descripcion": "Creamos sitios web modernos, responsivos y optimizados para convertir visitantes en clientes.",
            "beneficios": [
                "Diseño 100% responsive para todos los dispositivos",
                "Optimización SEO para mejor posicionamiento",
                "Velocidad de carga optimizada",
                "Integración con WooCommerce para e-commerce",
                "Certificados SSL y medidas de seguridad"
            ],
            "paquetes": {
                "presencial": {
                    "nombre": "Web Presencial",
                    "descripcion": "Ideal para profesionales y pequeñas empresas",
                    "caracteristicas": [
                        "Página web informativa hasta 5 secciones",
                        "Diseño responsive",
                        "Integración de formulario de contacto",
                        "Optimización SEO básica",
                        "Dominio y hosting por 1 año incluido",
                        "Soporte técnico básico por 1 mes"
                    ]
                },
                "negocio": {
                    "nombre": "Web Negocio",
                    "descripcion": "Para empresas que buscan una página web dinámica",
                    "caracteristicas": [
                        "Página web con CMS para autogestión",
                        "Hasta 10 secciones y blog integrado",
                        "Diseño responsive y optimización de velocidad",
                        "Integración de redes sociales",
                        "Optimización SEO avanzada",
                        "Soporte técnico prioritario por 3 meses"
                    ]
                },
                "ecommerce": {
                    "nombre": "Web E-commerce",
                    "descripcion": "La solución perfecta para vender online",
                    "caracteristicas": [
                        "Tienda online completa con WooCommerce",
                        "Diseño personalizado y responsive",
                        "Configuración de hasta 50 productos",
                        "Integración de pasarelas de pago",
                        "Gestión de inventario y pedidos",
                        "Consultoría de marketing digital"
                    ]
                }
            }
        }
    },
    "contacto": {
        "email": "info@aiz-agencia.com",
        "telefono": "+52 (56) 32133454",
        "direccion": "Guanajuato 131-101 Col. Roma Norte Del. Cuauhtémoc CP 06700",
        "horarios": "Lunes a Viernes de 9:00 AM a 6:00 PM"
    }
}

def get_response(user_message):
    """Genera una respuesta basada en el mensaje del usuario"""
    message = user_message.lower()
    
    # Saludos
    if any(word in message for word in ['hola', 'buenos días', 'buenas tardes', 'buenas noches', 'hi', 'hello']):
        return {
            "message": "¡Hola! Soy el asistente virtual de Aiz Agencia Digital. Estoy aquí para ayudarte con información sobre nuestros servicios de Agentes IA, Aplicaciones Móviles y Páginas Web. ¿En qué puedo ayudarte hoy?",
            "suggestions": ["Ver servicios", "Información de paquetes", "Contacto", "Cotización"]
        }
    
    # Servicios generales
    elif any(word in message for word in ['servicios', 'qué hacen', 'que ofrecen', 'información','sobre','acerca']):
        return {
            "message": "En Aiz Agencia Digital ofrecemos tres servicios principales:\n\n🤖 **Creación de Agentes IA** - Asistentes virtuales inteligentes\n📱 **Aplicaciones Móviles** - Apps nativas e híbridas\n💻 **Páginas Web** - Sitios modernos y e-commerce\n\n¿Te gustaría conocer más detalles sobre algún servicio en particular?",
            "suggestions": ["Agentes IA", "Apps Móviles", "Páginas Web", "e-commerce" "Ver todos los paquetes"]
        }
    
    # Agentes IA
    elif any(word in message for word in ['agente', 'ia', 'inteligencia artificial', 'chatbot', 'bot', 'agente conversacional']):
        service = knowledge_base["servicios"]["agentes_ia"]
        return {
            "message": f"🤖 **Creación de Agentes IA**\n\n{service['descripcion']}\n\n**Beneficios principales:**\n" + 
                      "\n".join([f"• {beneficio}" for beneficio in service['beneficios'][:3]]) +
                      "\n\n**Paquetes disponibles:**\n• Starter - Para pequeñas empresas\n• Pro - Solución completa\n• Empresarial - Transformación digital\n\n¿Te gustaría conocer más detalles sobre algún paquete?",
            "suggestions": ["Paquete Starter", "Paquete Pro", "Paquete Empresarial", "Cotizar Agente IA"]
        }
    
    # Apps móviles
    elif any(word in message for word in ['app', 'aplicación', 'móvil', 'android', 'ios']):
        service = knowledge_base["servicios"]["apps_moviles"]
        return {
            "message": f"📱 **Aplicaciones Móviles**\n\n{service['descripcion']}\n\n**Beneficios principales:**\n" + 
                      "\n".join([f"• {beneficio}" for beneficio in service['beneficios']]) +
                      "\n\n**Paquetes disponibles:**\n• Esencial - Presencia móvil básica\n• Avanzada - Experiencia mejorada\n• Empresarial - Solución escalable\n\n¿Qué tipo de aplicación tienes en mente?",
            "suggestions": ["App Esencial", "App Avanzada", "App Empresarial", "Cotizar App"]
        }
    
    # Páginas web
    elif any(word in message for word in ['web', 'página', 'sitio', 'website', 'ecommerce', 'tienda']):
        service = knowledge_base["servicios"]["paginas_web"]
        return {
            "message": f"💻 **Páginas Web**\n\n{service['descripcion']}\n\n**Beneficios principales:**\n" + 
                      "\n".join([f"• {beneficio}" for beneficio in service['beneficios']]) +
                      "\n\n**Paquetes disponibles:**\n• Presencial - Presencia online profesional\n• Negocio - Funcionalidades dinámicas\n• E-commerce - Tienda online completa\n\n¿Qué tipo de sitio web necesitas?",
            "suggestions": ["Web Presencial", "Web Negocio", "Web E-commerce", "Cotizar Web"]
        }
    
    # Paquetes específicos
    elif 'starter' in message or 'básico' in message:
        paquete = knowledge_base["servicios"]["agentes_ia"]["paquetes"]["starter"]
        return {
            "message": f"🤖 **{paquete['nombre']}**\n\n{paquete['descripcion']}\n\n**Incluye:**\n" + 
                      "\n".join([f"• {caracteristica}" for caracteristica in paquete['caracteristicas']]) +
                      "\n\n¿Te gustaría solicitar una cotización para este paquete?",
            "suggestions": ["Solicitar cotización", "Ver otros paquetes", "Contactar asesor", "Más información"]
        }
    
    # Contacto
    elif any(word in message for word in ['contacto', 'teléfono', 'email', 'dirección', 'ubicación']):
        contacto = knowledge_base["contacto"]
        return {
            "message": f"📞 **Información de Contacto**\n\n📧 **Email:** {contacto['info@aiz-agencia.com']}\n📱 **Teléfono:** {contacto['5632133454']}\n📍 **Dirección:** {contacto['Guanajuato 131-PB, Col. Roma']}\n🕒 **Horarios:** {contacto['Nuestros horarios son de 9:00 am a 6:00 pm']}\n\n¿Te gustaría que un asesor se ponga en contacto contigo?",
            "suggestions": ["Solicitar llamada", "Enviar email", "Agendar cita", "Ver ubicación"]
        }
    
    # Precios/Cotización
    elif any(word in message for word in ['precio', 'costo', 'cotización', 'presupuesto', 'cuánto']):
        return {
            "message": "💰 **Cotizaciones Personalizadas**\n\nNuestros precios varían según las necesidades específicas de cada proyecto. Ofrecemos:\n\n• **Consulta gratuita** para evaluar tu proyecto\n• **Cotizaciones personalizadas** sin compromiso\n• **Planes de pago flexibles**\n• **Garantía de satisfacción**\n\n¿Te gustaría agendar una consulta gratuita para recibir una cotización personalizada?",
            "suggestions": ["Agendar consulta", "Solicitar cotización", "Ver paquetes", "Hablar con asesor"]
        }
    
    # Despedida
    elif any(word in message for word in ['gracias', 'adiós', 'bye', 'hasta luego']):
        return {
            "message": "¡Gracias por tu interés en Aiz Agencia Digital! Ha sido un placer ayudarte. Si tienes más preguntas, no dudes en contactarnos:\n\n📧 info@aizagenciadigital.com\n📱 +52 (55) 1234 5678\n\n¡Esperamos trabajar contigo pronto! 🚀",
            "suggestions": ["Contactar ahora", "Ver servicios", "Solicitar cotización"]
        }
    
    # Respuesta por defecto
    else:
        return {
            "message": "Entiendo que estás interesado en nuestros servicios. Te puedo ayudar con información sobre:\n\n🤖 **Agentes IA** - Asistentes virtuales inteligentes\n📱 **Apps Móviles** - Aplicaciones nativas e híbridas\n💻 **Páginas Web** - Sitios modernos y e-commerce\n\n¿Sobre qué te gustaría saber más?",
            "suggestions": ["Agentes IA", "Apps Móviles", "Páginas Web", "Contacto"]
        }

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'Mensaje vacío'}), 400
        
        response = get_response(user_message)
        
        return jsonify({
            'success': True,
            'response': response['message'],
            'suggestions': response.get('suggestions', [])
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chatbot_bp.route('/chat/suggestions', methods=['GET'])
def get_suggestions():
    """Obtiene sugerencias iniciales para el chat"""
    return jsonify({
        'suggestions': [
            "¿Qué servicios ofrecen?",
            "Información sobre Agentes IA",
            "Quiero una app móvil",
            "Necesito una página web",
            "Solicitar cotización",
            "Información de contacto"
        ]
    })

