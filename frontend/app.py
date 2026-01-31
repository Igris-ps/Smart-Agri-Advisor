# ==================== SMART AGRI ADVISOR ====================
# AI-Powered Crop Advisory System for Farmers
# Features: Multilingual Support (Results included), Professional Colors
# =============================================================

# -------- STREAMLIT CLOUD IMPORT FIX (IMPORTANT) --------
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# -------------------------------------------------------

import streamlit as st
from datetime import datetime

# ==================== CONFIGURATION ====================
class Config:
    """Professional Color Configuration"""
    # Vibrant professional color palette
    PRIMARY_COLOR = "#00695C"  # Teal Green
    SECONDARY_COLOR = "#26A69A"  # Light Teal
    ACCENT_COLOR = "#80CBC4"  # Soft Teal
    
    ORANGE_PRIMARY = "#FF6F00"  # Vibrant Orange
    ORANGE_LIGHT = "#FFA726"  # Light Orange
    
    BLUE_PRIMARY = "#1976D2"  # Professional Blue
    BLUE_LIGHT = "#42A5F5"  # Light Blue
    
    PURPLE_PRIMARY = "#7B1FA2"  # Deep Purple
    PURPLE_LIGHT = "#BA68C8"  # Light Purple
    
    SUCCESS_COLOR = "#43A047"  # Green
    WARNING_COLOR = "#FB8C00"  # Orange
    DANGER_COLOR = "#E53935"  # Red
    INFO_COLOR = "#039BE5"  # Cyan
    
    # Background colors
    BACKGROUND_COLOR = "#F8F9FA"  # Light grey background
    CARD_BACKGROUND = "#FFFFFF"  # White cards
    GRADIENT_START = "#E0F2F1"  # Light teal
    GRADIENT_END = "#B2DFDB"  # Soft teal
    
    # Text colors
    TEXT_PRIMARY = "#263238"  # Dark blue-grey
    TEXT_SECONDARY = "#546E7A"  # Medium blue-grey
    TEXT_LIGHT = "#78909C"  # Light blue-grey
    TEXT_WHITE = "#FFFFFF"  # White
    
    # Effects
    SHADOW_LIGHT = "rgba(0, 0, 0, 0.08)"
    SHADOW_MEDIUM = "rgba(0, 0, 0, 0.15)"
    SHADOW_HEAVY = "rgba(0, 0, 0, 0.25)"

# ==================== TRANSLATIONS ====================
TRANSLATIONS = {
    "en": {
        # UI Elements
        "title": "🌾 Smart Agri Advisor",
        "subtitle": "AI-powered crop advisory system to help farmers identify diseases, pests, and irrigation problems",
        "input_header": "Tell Us About Your Crop Problem",
        "text_label": "Describe your problem",
        "text_placeholder": "Example: yellow spots on leaves, insects on crop, wilting plants",
        "image_label": "📷 Upload a photo of your crop",
        "voice_button": "Record Voice",
        "submit_button": "Get Expert Advice",
        "or_text": "OR",
        "success": "Analysis Completed Successfully",
        "language": "Language",
        "clear_button": "Clear All",
        "example_problems": "Common Crop Problems",
        "loading": "Analyzing your crop problem...",
        "call_support": "Call Support",
        "support_number": "1800-XXX-XXXX",
        "support_hours": "Available 24/7",
        
        # Results
        "analysis_title": "Detailed Analysis Report",
        "issue_header": "Identified Issue",
        "cause_header": "Possible Cause",
        "prevention_tips": "Prevention Tips",
        "chemical_treatment": "Chemical Treatment",
        "organic_treatment": "Organic Treatment",
        "immediate_action": "Immediate Action Required",
        
        # Result Content
        "leaf_blight_issue": "Leaf Blight Disease Detected",
        "leaf_blight_cause": "Caused by fungal pathogens, often due to excessive moisture and poor air circulation. This disease thrives in humid conditions and can spread rapidly if not addressed.",
        "leaf_blight_immediate": "Remove and destroy all infected leaves immediately to prevent disease spread. Isolate affected plants if possible.",
        
        "aphid_issue": "Aphid Infestation Detected",
        "aphid_cause": "Soft-bodied insects sucking plant sap, attracted to tender new growth. They multiply rapidly in warm conditions.",
        
        "nutrient_issue": "Nitrogen Deficiency Detected",
        "nutrient_cause": "Insufficient nitrogen in soil, often due to leaching or poor fertilization. Leaves turn yellow starting from older leaves.",
        
        # Treatments
        "organic_treatments": [
            "Apply neem oil spray every 7 days",
            "Use baking soda solution (1 tbsp per gallon)",
            "Copper-based organic fungicides",
            "Improve air circulation around plants"
        ],
        "chemical_treatments": [
            "Apply systemic fungicide as directed",
            "Use contact fungicide as preventive",
            "Consult agricultural extension office",
            "Follow proper application timing"
        ],
        "prevention_tips_list": [
            "Ensure proper spacing between plants",
            "Avoid overhead watering - use drip irrigation",
            "Remove crop debris after harvest",
            "Use disease-resistant varieties",
            "Practice crop rotation annually"
        ],
        
        "aphid_organic": [
            "Introduce ladybugs and lacewings",
            "Spray with soapy water solution",
            "Apply garlic-chili spray",
            "Use sticky yellow traps"
        ],
        "aphid_chemical": [
            "Insecticidal soap application",
            "Pyrethrin-based sprays",
            "Neem-based insecticides",
            "Systemic insecticides for severe cases"
        ],
        "aphid_prevention": [
            "Encourage beneficial insects",
            "Regular plant inspection",
            "Companion planting with marigolds",
            "Proper balanced fertilization",
            "Remove aphid-hosting weeds"
        ],
        
        "nutrient_organic": [
            "Apply well-composted manure",
            "Plant legume cover crops",
            "Use fish emulsion fertilizer",
            "Add grass clippings as mulch"
        ],
        "nutrient_chemical": [
            "Apply urea fertilizer (46-0-0)",
            "Use ammonium sulfate",
            "Slow-release nitrogen fertilizers",
            "Foliar nitrogen spray for quick results"
        ],
        "nutrient_prevention": [
            "Regular soil testing (twice yearly)",
            "Crop rotation with legumes",
            "Proper composting practices",
            "Balanced fertilization schedule",
            "Maintain proper soil pH"
        ],
    },
    "hi": {
        # UI Elements
        "title": "🌾 स्मार्ट कृषि सलाहकार",
        "subtitle": "रोगों, कीटों और सिंचाई समस्याओं की पहचान के लिए AI-संचालित फसल सलाहकार प्रणाली",
        "input_header": "अपनी फसल की समस्या के बारे में बताएं",
        "text_label": "अपनी समस्या का वर्णन करें",
        "text_placeholder": "उदाहरण: पत्तियों पर पीले धब्बे, फसल पर कीड़े, पौधे मुरझा रहे हैं",
        "image_label": "📷 अपनी फसल की फोटो अपलोड करें",
        "voice_button": "आवाज रिकॉर्ड करें",
        "submit_button": "विशेषज्ञ सलाह प्राप्त करें",
        "or_text": "या",
        "success": "विश्लेषण सफलतापूर्वक पूर्ण",
        "language": "भाषा",
        "clear_button": "सभी साफ करें",
        "example_problems": "सामान्य फसल समस्याएं",
        "loading": "आपकी फसल की समस्या का विश्लेषण किया जा रहा है...",
        "call_support": "सहायता कॉल करें",
        "support_number": "1800-XXX-XXXX",
        "support_hours": "24/7 उपलब्ध",
        
        # Results
        "analysis_title": "विस्तृत विश्लेषण रिपोर्ट",
        "issue_header": "पहचानी गई समस्या",
        "cause_header": "संभावित कारण",
        "prevention_tips": "रोकथाम सुझाव",
        "chemical_treatment": "रासायनिक उपचार",
        "organic_treatment": "जैविक उपचार",
        "immediate_action": "तत्काल कार्रवाई आवश्यक",
        
        # Result Content
        "leaf_blight_issue": "पत्ती झुलसा रोग का पता चला",
        "leaf_blight_cause": "फफूंदी रोगजनकों के कारण होता है, अक्सर अत्यधिक नमी और खराब वायु संचार के कारण। यह रोग आर्द्र परिस्थितियों में पनपता है और यदि समाधान नहीं किया गया तो तेजी से फैल सकता है।",
        "leaf_blight_immediate": "रोग के प्रसार को रोकने के लिए सभी संक्रमित पत्तियों को तुरंत हटा दें और नष्ट कर दें। यदि संभव हो तो प्रभावित पौधों को अलग कर दें।",
        
        "aphid_issue": "एफिड संक्रमण का पता चला",
        "aphid_cause": "कोमल शरीर वाले कीड़े पौधे का रस चूसते हैं, कोमल नई वृद्धि की ओर आकर्षित होते हैं। वे गर्म परिस्थितियों में तेजी से गुणा करते हैं।",
        
        "nutrient_issue": "नाइट्रोजन की कमी का पता चला",
        "nutrient_cause": "मिट्टी में नाइट्रोजन की कमी, अक्सर रिसाव या खराब उर्वरीकरण के कारण। पुरानी पत्तियों से शुरू होकर पत्तियां पीली हो जाती हैं।",
        
        # Treatments
        "organic_treatments": [
            "हर 7 दिन में नीम का तेल स्प्रे करें",
            "बेकिंग सोडा घोल का उपयोग करें (1 बड़ा चम्मच प्रति गैलन)",
            "तांबा आधारित जैविक कवकनाशी",
            "पौधों के आसपास वायु संचार में सुधार करें"
        ],
        "chemical_treatments": [
            "निर्देशानुसार प्रणालीगत कवकनाशी लगाएं",
            "निवारक के रूप में संपर्क कवकनाशी का उपयोग करें",
            "कृषि विस्तार कार्यालय से परामर्श लें",
            "उचित अनुप्रयोग समय का पालन करें"
        ],
        "prevention_tips_list": [
            "पौधों के बीच उचित दूरी सुनिश्चित करें",
            "ऊपर से पानी देने से बचें - ड्रिप सिंचाई का उपयोग करें",
            "फसल कटाई के बाद मलबा हटा दें",
            "रोग प्रतिरोधी किस्मों का उपयोग करें",
            "वार्षिक फसल चक्र का अभ्यास करें"
        ],
        
        "aphid_organic": [
            "लेडीबग और लेसविंग पेश करें",
            "साबुन के पानी के घोल से स्प्रे करें",
            "लहसुन-मिर्च स्प्रे लगाएं",
            "चिपचिपे पीले जाल का उपयोग करें"
        ],
        "aphid_chemical": [
            "कीटनाशक साबुन का अनुप्रयोग",
            "पाइरेथ्रिन आधारित स्प्रे",
            "नीम आधारित कीटनाशक",
            "गंभीर मामलों के लिए प्रणालीगत कीटनाशक"
        ],
        "aphid_prevention": [
            "लाभकारी कीड़ों को प्रोत्साहित करें",
            "नियमित पौधे निरीक्षण",
            "गेंदा के साथ साथी रोपण",
            "उचित संतुलित उर्वरीकरण",
            "एफिड-होस्टिंग खरपतवार हटाएं"
        ],
        
        "nutrient_organic": [
            "अच्छी तरह से कम्पोस्ट की गई खाद लगाएं",
            "फलीदार कवर फसलें लगाएं",
            "मछली इमल्शन उर्वरक का उपयोग करें",
            "घास की कतरन को गीली घास के रूप में डालें"
        ],
        "nutrient_chemical": [
            "यूरिया उर्वरक लगाएं (46-0-0)",
            "अमोनियम सल्फेट का उपयोग करें",
            "धीमी गति से रिलीज नाइट्रोजन उर्वरक",
            "त्वरित परिणामों के लिए पत्तेदार नाइट्रोजन स्प्रे"
        ],
        "nutrient_prevention": [
            "नियमित मिट्टी परीक्षण (वर्ष में दो बार)",
            "फलीदार के साथ फसल चक्र",
            "उचित खाद बनाने की प्रथाएं",
            "संतुलित उर्वरीकरण अनुसूची",
            "उचित मिट्टी पीएच बनाए रखें"
        ],
    },
    "te": {
        # UI Elements
        "title": "🌾 స్మార్ట్ అగ్రి అడ్వైజర్",
        "subtitle": "వ్యాధులు, తెగులు మరియు నీటిపారుదల సమస్యలను గుర్తించడానికి AI-ఆధారిత పంట సలహా వ్యవస్థ",
        "input_header": "మీ పంట సమస్య గురించి చెప్పండి",
        "text_label": "మీ సమస్యను వివరించండి",
        "text_placeholder": "ఉదాహరణ: ఆకులపై పసుపు మచ్చలు, పంటపై కీటకాలు, మొక్కలు వాడిపోతున్నాయి",
        "image_label": "📷 మీ పంట ఫోటో అప్‌లోడ్ చేయండి",
        "voice_button": "వాయిస్ రికార్డ్ చేయండి",
        "submit_button": "నిపుణుల సలహా పొందండి",
        "or_text": "లేదా",
        "success": "విశ్లేషణ విజయవంతంగా పూర్తయింది",
        "language": "భాష",
        "clear_button": "అన్నింటినీ క్లియర్ చేయండి",
        "example_problems": "సాధారణ పంట సమస్యలు",
        "loading": "మీ పంట సమస్యను విశ్లేషిస్తోంది...",
        "call_support": "మద్దతు కాల్ చేయండి",
        "support_number": "1800-XXX-XXXX",
        "support_hours": "24/7 అందుబాటులో",
        
        # Results
        "analysis_title": "వివరణాత్మక విశ్లేషణ నివేదిక",
        "issue_header": "గుర్తించిన సమస్య",
        "cause_header": "సాధ్యమైన కారణం",
        "prevention_tips": "నివారణ చిట్కాలు",
        "chemical_treatment": "రసాయన చికిత్స",
        "organic_treatment": "సేంద్రీయ చికిత్స",
        "immediate_action": "తక్షణ చర్య అవసరం",
        
        # Result Content
        "leaf_blight_issue": "ఆకు మచ్చ వ్యాధి గుర్తించబడింది",
        "leaf_blight_cause": "శిలీంధ్ర రోగకారకాల వల్ల కలుగుతుంది, తరచుగా అధిక తేమ మరియు పేలవమైన గాలి ప్రసరణ కారణంగా. ఈ వ్యాధి తేమతో కూడిన పరిస్థితులలో వృద్ధి చెందుతుంది మరియు పరిష్కరించకపోతే వేగంగా వ్యాపిస్తుంది.",
        "leaf_blight_immediate": "వ్యాధి వ్యాప్తిని నివారించడానికి సోకిన ఆకులన్నింటినీ వెంటనే తొలగించి నాశనం చేయండి. సాధ్యమైతే ప్రభావిత మొక్కలను వేరు చేయండి.",
        
        "aphid_issue": "అఫిడ్ ముట్టడి గుర్తించబడింది",
        "aphid_cause": "మృదువైన శరీర కీటకాలు మొక్క రసాన్ని పీల్చుకుంటాయి, లేత కొత్త పెరుగుదలకు ఆకర్షితమవుతాయి. అవి వెచ్చని పరిస్థితులలో వేగంగా పెరుగుతాయి.",
        
        "nutrient_issue": "నైట్రోజన్ లోపం గుర్తించబడింది",
        "nutrient_cause": "మట్టిలో తగినంత నైట్రోజన్ లేకపోవడం, తరచుగా లీచింగ్ లేదా పేలవమైన ఫలదీకరణం కారణంగా. పాత ఆకుల నుండి ప్రారంభించి ఆకులు పసుపు రంగులోకి మారుతాయి.",
        
        # Treatments
        "organic_treatments": [
            "ప్రతి 7 రోజులకు వేప నూనె స్ప్రే వేయండి",
            "బేకింగ్ సోడా ద్రావణం ఉపయోగించండి (గాలన్‌కు 1 టేబుల్ స్పూన్)",
            "రాగి ఆధారిత సేంద్రీయ శిలీంధ్ర నాశనులు",
            "మొక్కల చుట్టూ గాలి ప్రసరణను మెరుగుపరచండి"
        ],
        "chemical_treatments": [
            "నిర్దేశించిన విధంగా వ్యవస్థాగత శిలీంధ్ర నాశకాన్ని వర్తింపజేయండి",
            "నివారణగా సంపర్క శిలీంధ్ర నాశకాన్ని ఉపయోగించండి",
            "వ్యవసాయ విస్తరణ కార్యాలయాన్ని సంప్రదించండి",
            "సరైన అప్లికేషన్ సమయాన్ని అనుసరించండి"
        ],
        "prevention_tips_list": [
            "మొక్కల మధ్య సరైన అంతరాన్ని నిర్ధారించండి",
            "పైనుండి నీరు పోయడం మానుకోండి - డ్రిప్ నీటిపారుదల ఉపయోగించండి",
            "పంట తర్వాత పంట వ్యర్థాలను తొలగించండి",
            "వ్యాధి నిరోధక రకాలను ఉపయోగించండి",
            "వార్షిక పంట భ్రమణాన్ని ఆచరించండి"
        ],
        
        "aphid_organic": [
            "లేడీబగ్స్ మరియు లేస్‌వింగ్స్‌ను పరిచయం చేయండి",
            "సబ్బు నీటి ద్రావణంతో స్ప్రే చేయండి",
            "వెల్లుల్లి-మిరపకాయ స్ప్రే వర్తించండి",
            "జిగురు పసుపు ఉచ్చులను ఉపయోగించండి"
        ],
        "aphid_chemical": [
            "క్రిమి నాశక సబ్బు అప్లికేషన్",
            "పైరెథ్రిన్ ఆధారిత స్ప్రేలు",
            "వేప ఆధారిత క్రిమి నాశకాలు",
            "తీవ్రమైన కేసుల కోసం వ్యవస్థాగత క్రిమి నాశకాలు"
        ],
        "aphid_prevention": [
            "ప్రయోజనకరమైన కీటకాలను ప్రోత్సహించండి",
            "క్రమం తప్పకుండా మొక్కల తనిఖీ",
            "మెరిగోల్డ్స్‌తో తోడు నాటడం",
            "సరైన సమతుల్య ఫలదీకరణం",
            "అఫిడ్-హోస్టింగ్ కలుపు మొక్కలను తొలగించండి"
        ],
        
        "nutrient_organic": [
            "బాగా కంపోస్ట్ చేసిన ఎరువును వర్తించండి",
            "పప్పుధాన్యాల కవర్ పంటలను నాటండి",
            "చేపల ఎమల్షన్ ఎరువును ఉపయోగించండి",
            "గడ్డి కోతలను మల్చ్‌గా జోడించండి"
        ],
        "nutrient_chemical": [
            "యూరియా ఎరువు వర్తించండి (46-0-0)",
            "అమ్మోనియం సల్ఫేట్ ఉపయోగించండి",
            "నెమ్మదిగా విడుదల చేసే నైట్రోజన్ ఎరువులు",
            "త్వరిత ఫలితాల కోసం ఆకు నైట్రోజన్ స్ప్రే"
        ],
        "nutrient_prevention": [
            "క్రమం తప్పకుండా మట్టి పరీక్ష (సంవత్సరానికి రెండుసార్లు)",
            "పప్పుధాన్యాలతో పంట భ్రమణం",
            "సరైన కంపోస్టింగ్ పద్ధతులు",
            "సమతుల్య ఫలదీకరణ షెడ్యూల్",
            "సరైన మట్టి pH నిర్వహించండి"
        ],
    },
}

EXAMPLE_PROBLEMS = {
    "en": [
        "Yellow spots on leaves",
        "Insects eating crops",
        "Plants wilting",
        "Brown patches on stems",
        "Holes in leaves",
        "White powdery coating",
        "Leaf curling",
        "Stunted growth",
    ],
    "hi": [
        "पत्तियों पर पीले धब्बे",
        "कीड़े फसल खा रहे हैं",
        "पौधे मुरझा रहे हैं",
        "तनों पर भूरे धब्बे",
        "पत्तियों में छेद",
        "सफेद पाउडरी कोटिंग",
        "पत्ती कर्लिंग",
        "अवरुद्ध विकास",
    ],
    "te": [
        "ఆకులపై పసుపు మచ్చలు",
        "కీటకాలు పంటలు తింటున్నాయి",
        "మొక్కలు వాడిపోతున్నాయి",
        "కాండాలపై గోధుమ మచ్చలు",
        "ఆకులలో రంధ్రాలు",
        "తెల్లటి పౌడర్ పూత",
        "ఆకు కర్లింగ్",
        "మందగమన వృద్ధి",
    ],
}

# ==================== CUSTOM CSS ====================
def load_custom_css():
    """Load vibrant professional CSS"""
    css = f"""
    <style>
    /* ========== IMPORT FONTS ========== */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');
    
    /* ========== ROOT VARIABLES ========== */
    :root {{
        --primary: {Config.PRIMARY_COLOR};
        --secondary: {Config.SECONDARY_COLOR};
        --accent: {Config.ACCENT_COLOR};
        --orange: {Config.ORANGE_PRIMARY};
        --orange-light: {Config.ORANGE_LIGHT};
        --blue: {Config.BLUE_PRIMARY};
        --blue-light: {Config.BLUE_LIGHT};
        --purple: {Config.PURPLE_PRIMARY};
        --purple-light: {Config.PURPLE_LIGHT};
        --success: {Config.SUCCESS_COLOR};
        --warning: {Config.WARNING_COLOR};
        --danger: {Config.DANGER_COLOR};
        --info: {Config.INFO_COLOR};
        --bg: {Config.BACKGROUND_COLOR};
        --card-bg: {Config.CARD_BACKGROUND};
        --text: {Config.TEXT_PRIMARY};
        --text-secondary: {Config.TEXT_SECONDARY};
        --text-light: {Config.TEXT_LIGHT};
        --text-white: {Config.TEXT_WHITE};
    }}
    
    /* ========== GLOBAL STYLES ========== */
    * {{
        font-family: 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif;
    }}
    
    .stApp {{
        background: linear-gradient(135deg, {Config.GRADIENT_START} 0%, var(--bg) 50%, {Config.GRADIENT_END} 100%);
        background-attachment: fixed;
    }}
    
    /* Fix all text colors */
    p, span, div, label, h1, h2, h3, h4, h5, h6, li, td, th {{
        color: var(--text) !important;
    }}
    
    /* ========== HEADER ========== */
    .main-header {{
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 50%, var(--accent) 100%);
        padding: 50px 30px;
        border-radius: 20px;
        margin-bottom: 35px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 105, 92, 0.3);
        position: relative;
        overflow: hidden;
    }}
    
    .main-header::before {{
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: rotate 20s linear infinite;
    }}
    
    @keyframes rotate {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
    }}
    
    .main-header h1 {{
        color: var(--text-white) !important;
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        margin-bottom: 15px !important;
        text-shadow: 2px 2px 12px rgba(0,0,0,0.3);
        position: relative;
        z-index: 1;
    }}
    
    .subtitle {{
        color: var(--text-white) !important;
        font-size: 1.4rem !important;
        max-width: 900px;
        margin: 0 auto;
        opacity: 0.95;
        font-weight: 500;
        line-height: 1.8;
        position: relative;
        z-index: 1;
    }}
    
    /* ========== CALL SUPPORT BUTTON ========== */
    .call-support-container {{
        position: fixed;
        bottom: 30px;
        right: 30px;
        z-index: 9999;
    }}
    
    .call-support-btn {{
        background: linear-gradient(135deg, var(--success) 0%, #2E7D32 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 20px 35px;
        font-size: 1.15rem;
        font-weight: 700;
        cursor: pointer;
        box-shadow: 0 10px 30px rgba(67, 160, 71, 0.4);
        display: flex;
        align-items: center;
        gap: 15px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        text-decoration: none;
        animation: pulse-glow 2s infinite;
    }}
    
    @keyframes pulse-glow {{
        0%, 100% {{ box-shadow: 0 10px 30px rgba(67, 160, 71, 0.4); }}
        50% {{ box-shadow: 0 10px 40px rgba(67, 160, 71, 0.6); }}
    }}
    
    .call-support-btn:hover {{
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 15px 40px rgba(67, 160, 71, 0.6);
    }}
    
    /* ========== SIDEBAR STYLING ========== */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, var(--card-bg) 0%, {Config.GRADIENT_START} 100%) !important;
    }}
    
    [data-testid="stSidebar"] > div:first-child {{
        background: linear-gradient(180deg, var(--card-bg) 0%, {Config.GRADIENT_START} 100%) !important;
    }}
    
    /* ========== INPUT SECTION ========== */
    .input-section {{
        background: var(--card-bg);
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 8px 25px {Config.SHADOW_MEDIUM};
        margin-bottom: 35px;
        border: 2px solid var(--accent);
    }}
    
    .section-title {{
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2rem !important;
        font-weight: 800 !important;
        margin-bottom: 25px !important;
        display: flex;
        align-items: center;
        gap: 15px;
    }}
    
    /* ========== TEXT AREA ========== */
    .stTextArea label {{
        color: var(--text) !important;
        font-weight: 700 !important;
        font-size: 1.15rem !important;
        margin-bottom: 12px !important;
    }}
    
    .stTextArea textarea {{
        background: var(--card-bg) !important;
        border: 3px solid var(--accent) !important;
        border-radius: 15px !important;
        padding: 20px !important;
        font-size: 1.1rem !important;
        color: var(--text) !important;
        transition: all 0.3s !important;
        line-height: 1.8 !important;
    }}
    
    .stTextArea textarea:focus {{
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 5px rgba(0, 105, 92, 0.15) !important;
        outline: none !important;
    }}
    
    .stTextArea textarea::placeholder {{
        color: var(--text-light) !important;
        opacity: 0.7 !important;
    }}
    
    /* ========== BUTTONS ========== */
    .stButton > button {{
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%) !important;
        color: var(--text-white) !important;
        font-size: 1.15rem !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 18px 35px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 6px 20px rgba(0, 105, 92, 0.3) !important;
        letter-spacing: 0.5px;
    }}
    
    .stButton > button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(0, 105, 92, 0.4) !important;
    }}
    
    /* ========== SELECT BOX ========== */
    .stSelectbox label {{
        color: var(--text) !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
    }}
    
    .stSelectbox > div > div {{
        background: var(--card-bg) !important;
        border: 2px solid var(--accent) !important;
        border-radius: 12px !important;
    }}
    
    /* Force select box text to be dark */
    .stSelectbox [data-baseweb="select"] {{
        background-color: var(--card-bg) !important;
    }}
    
    .stSelectbox [data-baseweb="select"] > div {{
        background-color: var(--card-bg) !important;
        color: var(--text) !important;
    }}
    
    .stSelectbox input {{
        color: var(--text) !important;
    }}
    
    /* Dropdown menu items */
    [data-baseweb="popover"] {{
        background-color: var(--card-bg) !important;
    }}
    
    [role="option"] {{
        background-color: var(--card-bg) !important;
        color: var(--text) !important;
    }}
    
    [role="option"]:hover {{
        background-color: var(--accent) !important;
        color: var(--text) !important;
    }}
    
    /* Selected option text */
    [data-baseweb="select"] span {{
        color: var(--text) !important;
    }}
    
    /* ========== EXAMPLE TAGS ========== */
    .example-tag {{
        display: inline-block;
        background: linear-gradient(135deg, var(--blue-light), var(--blue));
        color: var(--text-white);
        padding: 12px 24px;
        border-radius: 25px;
        margin: 8px;
        font-size: 1rem;
        cursor: pointer;
        transition: all 0.3s;
        border: none;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(25, 118, 210, 0.3);
    }}
    
    .example-tag:hover {{
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 6px 20px rgba(25, 118, 210, 0.5);
    }}
    
    /* ========== RESULT CARDS ========== */
    .result-card {{
        background: var(--card-bg);
        border-radius: 20px;
        padding: 30px;
        margin: 25px 0;
        box-shadow: 0 8px 25px {Config.SHADOW_MEDIUM};
        border-left: 6px solid var(--accent);
        transition: all 0.3s;
        position: relative;
        overflow: hidden;
    }}
    
    .result-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 6px;
        height: 100%;
        background: linear-gradient(180deg, var(--primary), var(--secondary), var(--accent));
    }}
    
    .result-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 12px 35px {Config.SHADOW_HEAVY};
    }}
    
    .result-card.organic {{
        border-left-color: var(--success);
    }}
    
    .result-card.organic::before {{
        background: linear-gradient(180deg, var(--success), #2E7D32);
    }}
    
    .result-card.chemical {{
        border-left-color: var(--info);
    }}
    
    .result-card.chemical::before {{
        background: linear-gradient(180deg, var(--info), #0277BD);
    }}
    
    .result-card.prevention {{
        border-left-color: var(--purple);
    }}
    
    .result-card.prevention::before {{
        background: linear-gradient(180deg, var(--purple), var(--purple-light));
    }}
    
    .result-title {{
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 1.6rem !important;
        font-weight: 800 !important;
        margin-bottom: 20px !important;
        display: flex;
        align-items: center;
        gap: 12px;
    }}
    
    .result-content {{
        color: var(--text) !important;
        font-size: 1.1rem !important;
        line-height: 1.9 !important;
        font-weight: 500;
    }}
    
    .result-list {{
        list-style: none;
        padding: 0;
        margin: 15px 0;
    }}
    
    .result-list li {{
        background: linear-gradient(90deg, rgba(0, 105, 92, 0.05), transparent);
        padding: 15px 20px;
        margin: 10px 0;
        border-radius: 10px;
        border-left: 4px solid var(--accent);
        color: var(--text) !important;
        font-weight: 500;
        transition: all 0.3s;
    }}
    
    .result-list li:hover {{
        background: linear-gradient(90deg, rgba(0, 105, 92, 0.1), transparent);
        border-left-color: var(--primary);
        transform: translateX(5px);
    }}
    
    /* ========== SEVERITY BADGES ========== */
    .severity-badge {{
        display: inline-flex;
        align-items: center;
        padding: 8px 20px;
        border-radius: 25px;
        font-size: 0.9rem;
        font-weight: 800;
        letter-spacing: 1px;
        text-transform: uppercase;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }}
    
    .severity-low {{ 
        background: linear-gradient(135deg, #66BB6A, var(--success));
        color: var(--text-white);
    }}
    
    .severity-medium {{ 
        background: linear-gradient(135deg, var(--orange-light), var(--orange));
        color: var(--text-white);
    }}
    
    .severity-high {{ 
        background: linear-gradient(135deg, #EF5350, var(--danger));
        color: var(--text-white);
    }}
    
    /* ========== FILE UPLOADER ========== */
    .stFileUploader label {{
        color: var(--text) !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
    }}
    
    .stFileUploader > section {{ 
        background: var(--card-bg) !important;
        border: 3px dashed var(--accent) !important;
        border-radius: 20px !important;
        padding: 35px !important;
        transition: all 0.3s !important;
    }}
    
    .stFileUploader > section:hover {{
        border-color: var(--primary) !important;
        background: {Config.GRADIENT_START} !important;
        transform: scale(1.02);
    }}
    
    /* ========== VOICE CARD ========== */
    .voice-card {{
        background: linear-gradient(135deg, var(--orange) 0%, var(--orange-light) 100%);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(255, 111, 0, 0.3);
        margin-bottom: 20px;
        position: relative;
        overflow: hidden;
    }}
    
    .voice-card::before {{
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, transparent 70%);
        animation: rotate 15s linear infinite;
    }}
    
    .voice-card h4 {{
        color: var(--text-white) !important;
        margin: 0 0 15px 0 !important;
        font-size: 1.5rem !important;
        font-weight: 800 !important;
        position: relative;
        z-index: 1;
    }}
    
    .voice-card p {{
        color: var(--text-white) !important;
        opacity: 0.95;
        margin: 10px 0;
        position: relative;
        z-index: 1;
        font-weight: 500;
    }}
    
    .mic-button {{
        background: var(--text-white);
        color: var(--orange);
        border: none;
        border-radius: 50%;
        width: 80px;
        height: 80px;
        font-size: 2.5rem;
        cursor: pointer;
        margin: 20px auto;
        display: block;
        transition: all 0.3s;
        box-shadow: 0 6px 20px rgba(0,0,0,0.2);
        position: relative;
        z-index: 1;
    }}
    
    .mic-button:hover {{
        transform: scale(1.15);
        box-shadow: 0 8px 30px rgba(0,0,0,0.3);
    }}
    
    /* ========== OR DIVIDER ========== */
    .or-divider {{
        text-align: center;
        margin: 35px 0;
        position: relative;
    }}
    
    .or-divider::before {{
        content: '';
        position: absolute;
        left: 0;
        right: 0;
        top: 50%;
        height: 2px;
        background: linear-gradient(90deg, transparent, var(--accent), transparent);
    }}
    
    .or-divider span {{
        background: var(--card-bg);
        padding: 0 25px;
        position: relative;
        color: var(--text) !important;
        font-weight: 800;
        font-size: 1.3rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }}
    
    /* ========== METRICS ========== */
    [data-testid="stMetricValue"] {{
        color: var(--primary) !important;
        font-size: 2rem !important;
        font-weight: 900 !important;
    }}
    
    [data-testid="stMetricLabel"] {{
        color: var(--text-secondary) !important;
        font-weight: 700 !important;
        font-size: 0.9rem !important;
    }}
    
    /* ========== EXPANDER ========== */
    .streamlit-expanderHeader {{
        background: linear-gradient(135deg, {Config.GRADIENT_START}, var(--card-bg)) !important;
        border-radius: 15px !important;
        padding: 18px !important;
        font-weight: 700 !important;
        color: var(--text) !important;
        border: 2px solid var(--accent);
        transition: all 0.3s;
    }}
    
    .streamlit-expanderHeader:hover {{
        background: linear-gradient(135deg, var(--accent), {Config.GRADIENT_START}) !important;
        border-color: var(--primary);
        transform: translateY(-2px);
    }}
    
    /* ========== SUCCESS/INFO ALERTS ========== */
    .stSuccess {{
        background: linear-gradient(135deg, #E8F5E9, #C8E6C9) !important;
        color: #1B5E20 !important;
        border-left: 6px solid var(--success) !important;
        padding: 25px !important;
        border-radius: 15px !important;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(67, 160, 71, 0.2);
    }}
    
    .stWarning {{
        background: linear-gradient(135deg, #FFF3E0, #FFE0B2) !important;
        color: #E65100 !important;
        border-left: 6px solid var(--warning) !important;
        padding: 25px !important;
        border-radius: 15px !important;
        font-weight: 600;
    }}
    
    /* ========== FOOTER ========== */
    .app-footer {{
        text-align: center;
        padding: 45px 25px;
        background: var(--card-bg);
        border-radius: 20px;
        margin-top: 60px;
        border: 2px solid var(--accent);
        box-shadow: 0 8px 25px {Config.SHADOW_MEDIUM};
    }}
    
    .footer-links {{
        display: flex;
        justify-content: center;
        gap: 50px;
        margin-bottom: 25px;
        flex-wrap: wrap;
    }}
    
    .footer-link {{
        color: var(--text) !important;
        font-weight: 700;
        font-size: 1.05rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }}
    
    /* ========== RESPONSIVE ========== */
    @media (max-width: 768px) {{
        .main-header h1 {{
            font-size: 2.5rem !important;
        }}
        
        .subtitle {{
            font-size: 1.1rem !important;
        }}
        
        .call-support-container {{
            bottom: 20px;
            right: 20px;
        }}
        
        .call-support-btn {{
            padding: 15px 25px;
            font-size: 1rem;
        }}
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# ==================== HELPER FUNCTIONS ====================
def get_text(key):
    """Get translated text"""
    lang = st.session_state.get("language", "en")
    return TRANSLATIONS.get(lang, TRANSLATIONS["en"]).get(key, key)

def initialize_session_state():
    """Initialize session state"""
    defaults = {
        "language": "en",
        "query": "",
        "results": None,
        "show_results": False
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

# ==================== COMPONENTS ====================
def create_header():
    """Create header"""
    st.markdown(f"""
    <div class="main-header">
        <h1>{get_text('title')}</h1>
        <p class="subtitle">{get_text('subtitle')}</p>
    </div>
    """, unsafe_allow_html=True)

def create_call_support_button():
    """Create call support button"""
    st.markdown(f"""
    <div class="call-support-container">
        <a href="tel:{get_text('support_number')}" class="call-support-btn">
            <span style="font-size: 1.8rem;">📞</span>
            <div>
                <div style="font-size: 0.75rem; opacity: 0.9; font-weight: 500;">{get_text('support_hours')}</div>
                <div style="font-size: 1.15rem;">{get_text('call_support')}</div>
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)

def create_sidebar():
    """Create sidebar"""
    with st.sidebar:
        # Logo
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 35px; padding: 25px; background: var(--card-bg); border-radius: 20px; box-shadow: 0 4px 15px {Config.SHADOW_LIGHT}; border: 2px solid var(--accent);">
            <div style="background: linear-gradient(135deg, {Config.PRIMARY_COLOR}, {Config.SECONDARY_COLOR}); 
                        width: 90px; 
                        height: 90px; 
                        border-radius: 20px; 
                        display: inline-flex; 
                        align-items: center; 
                        justify-content: center;
                        font-size: 3rem;
                        color: white;
                        margin-bottom: 15px;
                        box-shadow: 0 6px 20px rgba(0, 105, 92, 0.4);">
                🌾
            </div>
            <h2 style="color: {Config.PRIMARY_COLOR}; margin: 0; font-weight: 900; font-size: 1.7rem;">Agri Advisor</h2>
            <p style="color: {Config.TEXT_SECONDARY}; font-size: 0.9rem; margin: 8px 0 0 0; font-weight: 600;">Smart Farming Solutions</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Language selection
        st.markdown(f"### {get_text('language')}")
        language_options = {
            "en": "🇬🇧 English",
            "hi": "🇮🇳 हिन्दी",
            "te": "🇮🇳 తెలుగు",
        }
        
        selected_lang = st.selectbox(
            "Select Language",
            options=list(language_options.keys()),
            format_func=lambda x: language_options[x],
            label_visibility="collapsed",
            index=list(language_options.keys()).index(st.session_state.language)
        )
        
        if selected_lang != st.session_state.language:
            st.session_state.language = selected_lang
            st.rerun()
        
        st.markdown("---")
        
        # Quick stats
        st.markdown("### 📊 Platform Stats")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("🌱", "25+", "Crops")
        with col2:
            st.metric("🐛", "100+", "Pests")
        with col3:
            st.metric("💧", "50+", "Issues")
        
        st.markdown("---")
        
        # Features
        st.markdown("### ✨ Features")
        features = [
            ("🔍", "Disease Detection"),
            ("🌱", "Growth Monitoring"),
            ("💧", "Irrigation Advice"),
            ("🧪", "Treatment Plans"),
            ("📊", "Weather Insights"),
            ("🌾", "Crop Rotation"),
        ]
        
        for icon, feature in features:
            st.markdown(f"""
            <div style="padding: 12px; margin: 8px 0; background: var(--card-bg); border-radius: 12px; 
                        display: flex; align-items: center; gap: 12px; border: 2px solid var(--accent);
                        box-shadow: 0 2px 8px {Config.SHADOW_LIGHT}; transition: all 0.3s;"
                 onmouseover="this.style.transform='translateX(5px)'; this.style.borderColor='{Config.PRIMARY_COLOR}';"
                 onmouseout="this.style.transform='translateX(0px)'; this.style.borderColor='{Config.ACCENT_COLOR}';">
                <span style="font-size: 1.5rem;">{icon}</span>
                <span style="color: {Config.TEXT_PRIMARY}; font-weight: 700; font-size: 0.95rem;">{feature}</span>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Support
        st.markdown("### 📞 Need Help?")
        st.info(f"""
        **Helpline:** {get_text('support_number')}  
        **Email:** support@agriadvisor.com  
        **Hours:** {get_text('support_hours')}
        """)

def create_input_section():
    """Create input section"""
    st.markdown(f"""
    <div class="input-section">
        <h2 class="section-title">📝 {get_text('input_header')}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Example problems
    with st.expander(f"💡 {get_text('example_problems')}", expanded=False):
        lang = st.session_state.get("language", "en")
        examples = EXAMPLE_PROBLEMS.get(lang, EXAMPLE_PROBLEMS["en"])
        
        tags_html = "<div style='margin: 20px 0; text-align: center;'>"
        for example in examples:
            tags_html += f"<span class='example-tag'>{example}</span>"
        tags_html += "</div>"
        st.markdown(tags_html, unsafe_allow_html=True)
    
    # Text input
    query = st.text_area(
        get_text("text_label"),
        value=st.session_state.get("query", ""),
        placeholder=get_text("text_placeholder"),
        height=150,
        key="text_input"
    )
    
    # OR divider
    st.markdown(f"""
    <div class="or-divider">
        <span>{get_text('or_text')}</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Voice and Image
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="voice-card">
            <h4>🎤 {get_text('voice_button')}</h4>
            <p>Click microphone to record</p>
            <button class="mic-button" onclick="alert('Voice feature coming soon!')">🎤</button>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        image = st.file_uploader(
            get_text("image_label"),
            type=["jpg", "jpeg", "png"]
        )
        
        if image is not None:
            st.image(image, caption="📸 Uploaded Image", use_container_width=True)
    
    return query, image

def create_result_display(result):
    """Create result display with multilingual content"""
    # Success message
    st.success(f"✅ {get_text('success')}")
    
    # Analysis header
    severity = result.get("severity", "medium")
    severity_text = {"low": "Low", "medium": "Medium", "high": "High"}.get(severity, "Medium")
    
    st.markdown(f"""
    <div style="background: var(--card-bg); padding: 30px; border-radius: 20px; 
                margin: 25px 0; box-shadow: 0 8px 25px {Config.SHADOW_MEDIUM}; border: 2px solid var(--accent);">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px;">
            <h2 style="color: {Config.PRIMARY_COLOR}; margin: 0; font-size: 2rem; font-weight: 900;">
                📊 {get_text('analysis_title')}
            </h2>
            <span class="severity-badge severity-{severity}">
                {severity_text}
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Issue card
    st.markdown(f"""
    <div class="result-card">
        <div class="result-title">🔍 {get_text('issue_header')}</div>
        <p class="result-content">{get_text(result['issue_key'])}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Cause card
    st.markdown(f"""
    <div class="result-card">
        <div class="result-title">📌 {get_text('cause_header')}</div>
        <p class="result-content">{get_text(result['cause_key'])}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Immediate action for high severity
    if severity == "high":
        st.markdown(f"""
        <div class="result-card" style="border-left-color: {Config.DANGER_COLOR}; background: linear-gradient(135deg, #FFEBEE, var(--card-bg));">
            <div class="result-title" style="background: linear-gradient(135deg, {Config.DANGER_COLOR}, #E53935); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                ⚡ {get_text('immediate_action')}
            </div>
            <p class="result-content" style="color: #C62828; font-weight: 700;">
                {get_text(result.get('immediate_key', 'leaf_blight_immediate'))}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Treatments
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="result-card organic">
            <div class="result-title" style="background: linear-gradient(135deg, {Config.SUCCESS_COLOR}, #2E7D32); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                🌿 {get_text('organic_treatment')}
            </div>
            <ul class="result-list">
        """, unsafe_allow_html=True)
        for treatment in get_text(result['organic_key']):
            st.markdown(f"<li>{treatment}</li>", unsafe_allow_html=True)
        st.markdown("</ul></div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="result-card chemical">
            <div class="result-title" style="background: linear-gradient(135deg, {Config.INFO_COLOR}, #0277BD); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                🧪 {get_text('chemical_treatment')}
            </div>
            <ul class="result-list">
        """, unsafe_allow_html=True)
        for treatment in get_text(result['chemical_key']):
            st.markdown(f"<li>{treatment}</li>", unsafe_allow_html=True)
        st.markdown("</ul></div>", unsafe_allow_html=True)
    
    # Prevention tips
    st.markdown(f"""
    <div class="result-card prevention">
        <div class="result-title" style="background: linear-gradient(135deg, {Config.PURPLE_PRIMARY}, {Config.PURPLE_LIGHT}); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            📋 {get_text('prevention_tips')}
        </div>
        <ul class="result-list">
    """, unsafe_allow_html=True)
    
    for tip in get_text(result['prevention_key']):
        st.markdown(f"<li>{tip}</li>", unsafe_allow_html=True)
    
    st.markdown("</ul></div>", unsafe_allow_html=True)

def create_footer():
    """Create footer"""
    st.markdown(f"""
    <div class="app-footer">
        <div class="footer-links">
            <span class="footer-link">🌾 AI-Powered</span>
            <span class="footer-link">🌱 Farmer First</span>
            <span class="footer-link">💧 Water Efficient</span>
        </div>
        <p style="color: {Config.TEXT_SECONDARY}; margin: 20px 0; font-size: 1.05rem; font-weight: 600;">
            © 2024 Smart Agri Advisor • Built with ❤️ for Farmers
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==================== MOCK DATA ====================
def generate_mock_advice(problem_type):
    """Generate mock advice"""
    mock_data = {
        "disease": {
            "issue_key": "leaf_blight_issue",
            "cause_key": "leaf_blight_cause",
            "immediate_key": "leaf_blight_immediate",
            "severity": "high",
            "organic_key": "organic_treatments",
            "chemical_key": "chemical_treatments",
            "prevention_key": "prevention_tips_list"
        },
        "pest": {
            "issue_key": "aphid_issue",
            "cause_key": "aphid_cause",
            "severity": "medium",
            "organic_key": "aphid_organic",
            "chemical_key": "aphid_chemical",
            "prevention_key": "aphid_prevention"
        },
        "nutrient": {
            "issue_key": "nutrient_issue",
            "cause_key": "nutrient_cause",
            "severity": "medium",
            "organic_key": "nutrient_organic",
            "chemical_key": "nutrient_chemical",
            "prevention_key": "nutrient_prevention"
        }
    }
    
    return mock_data.get(problem_type, mock_data["disease"])

# ==================== MAIN APP ====================
def main():
    st.set_page_config(
        page_title="Smart Agri Advisor",
        page_icon="🌾",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    load_custom_css()
    initialize_session_state()
    create_sidebar()
    create_call_support_button()
    
    # Main content
    col1, col2, col3 = st.columns([1, 10, 1])
    
    with col2:
        create_header()
        query, image = create_input_section()
        
        # Submit button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button(
                f"🚀 {get_text('submit_button')}", 
                use_container_width=True,
                type="primary"
            ):
                if query or image:
                    with st.spinner(f"🌾 {get_text('loading')}"):
                        import time
                        time.sleep(1.5)
                        
                        # Determine problem type
                        problem_type = "disease"
                        if query:
                            query_lower = query.lower()
                            if "insect" in query_lower or "pest" in query_lower or "bug" in query_lower or "aphid" in query_lower:
                                problem_type = "pest"
                            elif "yellow" in query_lower or "nitrogen" in query_lower or "nutrient" in query_lower:
                                problem_type = "nutrient"
                        
                        result = generate_mock_advice(problem_type)
                        st.session_state.results = result
                        st.session_state.show_results = True
                        st.rerun()
                else:
                    st.warning("⚠️ Please provide a description or upload an image!")
        
        # Display results
        if st.session_state.get("show_results") and st.session_state.get("results"):
            st.markdown("<br>", unsafe_allow_html=True)
            create_result_display(st.session_state.results)
        
        # Footer
        st.markdown("<br><br>", unsafe_allow_html=True)
        create_footer()

if __name__ == "__main__":
    main()