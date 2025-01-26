import streamlit as st
from streamlit.components.v1 import html

def main():
    # Page configuration
    st.set_page_config(
        page_title="nexspace Demo",
        page_icon="🏢",
        layout="centered"
    )

    # Header
    st.title("nexspace Service Explorer")
    st.subheader("Entdecken Sie unsere Colocation und Datacenter Lösungen")

    # Main content sections using tabs
    tabs = st.tabs(["Services", "Chat Demo", "Prompt Documentation"])
    
    with tabs[0]:
        st.markdown("""
        ### Unsere Kernservices
        
        #### 🏢 Colocation Services
        - Höheneinheiten, Cabinets und Käfige
        - Flexible Skalierung
        - 24/7 Support
        
        #### 🔒 Sicherheit & Compliance
        - GDPR-konform
        - ISO 27001
        - SOC 2
        
        #### 💡 Technische Infrastruktur
        - Hochverfügbare Netzwerkanbindung
        - Redundante Stromversorgung
        - Modernste Kühlung
        """)

    with tabs[1]:
        st.markdown("### Sprechen Sie mit unserem nex-Guide")
        # Feazy Chat Component
        chat_html = '''
        <div id="chat-container" style="height: 600px;">
        <script type="module" src="https://unpkg.com/feazy-plugin/dist/feazy-chat-component.es.js"></script>
        <chat-component 
            theme="neutral-theme"
            promptId="77632046-81f6-4cc0-9681-ebc20f55389b"
            chatTitle="nex-Guide"
            showDataProtection="true"
            isDialogVisible="true"
            baseUrl="https://api.feazy.ai"
            id="nexspace-bot">
        </chat-component>
        
        <style>
            chat-component {
                --primary-color: #2C3E50;
                --secondary-color: #f8f9fa;
                --text-color: #333333;
                --border-color: #dee2e6;
                --bot-message-bg: #f1f3f5;
                --user-message-bg: #e9ecef;
                --header-bg: #2C3E50;
                --header-text: #ffffff;
                --chat-button-bg: #2C3E50;
                --chat-button-color: #ffffff;
                --send-button-bg: #2C3E50;
                --send-button-color: #ffffff;
            }
        </style>
        </div>
        '''
        html(chat_html, height=650)

    with tabs[2]:
        st.markdown("### nex-Guide Prompt Konfiguration")
        with st.expander("Allgemeine Informationen"):
            st.markdown("""
            **Name:** nex-Guide Chatbot
            
            **Beschreibung:** Ein spezialisierter Assistent für nexspace, der Nutzer bei der Exploration von Colocation-Services und Datacenter-Lösungen unterstützt.
            """)
            
        with st.expander("Zielgruppen"):
            st.markdown("""
            **3rd Level Personas:**
            - IT-Leiter/CTO
            - IT-Administrator
            - CFO/Finanzleiter
            - Datenschutzbeauftragter
            - CEO/Unternehmer
            - Managed Service Provider
            
            **1st/2nd Level Personas:**
            - Startups und KMUs
            - Berater und IT-Dienstleister
            - Branchenvertreter
            
            **Bewerber/innen Personas:**
            - 1st Level: Überblick
            - 2nd Level: Spezifische Fragen
            - 3rd Level: Vertiefende Informationen
            """)
            
        with st.expander("Aufgaben & Funktionen"):
            st.markdown("""
            **Kernaufgaben:**
            1. Informationen zu Services bereitstellen
            2. Nutzer zu passenden Ressourcen führen
            3. Spezifische Fragen beantworten
            4. Verbindung zum nexspace-Team herstellen
            
            **Details zu Angeboten:**
            - Colocation Services
            - Sicherheit & Compliance
            - Technische Infrastruktur
            - Administrative Unterstützung
            """)

if __name__ == "__main__":
    main()