#!/usr/bin/env python3
"""
Author Identification Visualization App

Streamlit app to display author identification visualizations:
- Algazi book similarity heatmap
- Karkash book similarity heatmap
- Author chunk evaluation (index vs median similarity)
"""

import streamlit as st
from pathlib import Path
import re

# Set page configuration - hide sidebar
st.set_page_config(
    page_title="Author Identification Visualizations",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide the sidebar
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# Define file paths
BASE_DIR = Path(__file__).parent
ALGAZI_HTML = BASE_DIR / "inference" / "output" / "algazi_book_similarity_heatmap.html"
KARKASH_HTML = BASE_DIR / "inference" / "output" / "karkash_book_similarity_heatmap.html"
AUTHOR_EVAL_HTML = BASE_DIR / "evaluation" / "output" / "author_chunk_index_vs_median.html"

def load_html_file(file_path: Path, modify_karkash_labels=False):
    """Load HTML file content and optionally modify Karkash labels"""
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # If this is Krakash and we need to fix labels
        if modify_karkash_labels:
            # Use JavaScript injection to modify Plotly layout after it loads
            # This is more reliable than regex replacement which can break HTML
            # Add significant margin to prevent labels from being cut off
            js_injection = """
            <script>
            (function() {
                function rotateXAxisLabels() {
                    if (typeof Plotly !== 'undefined') {
                        var plots = document.querySelectorAll('.js-plotly-plot');
                        plots.forEach(function(plotDiv) {
                            if (plotDiv && plotDiv.data) {
                                // Update layout with margins and angle
                                var update = {
                                    'xaxis.tickangle': -45,
                                    'margin.b': 200,  // Increased bottom margin for angled labels
                                    'margin.r': 50,   // Right margin
                                    'margin.l': 200,  // Increased left margin for y-axis labels (long Hebrew names)
                                    'margin.t': 50    // Top margin
                                };
                                Plotly.relayout(plotDiv, update);
                                
                                // Also ensure container has enough padding on all sides
                                var container = plotDiv;
                                while (container && container.parentElement) {
                                    container.style.paddingBottom = '50px';
                                    container.style.paddingLeft = '20px';
                                    container.style.overflow = 'visible';
                                    container = container.parentElement;
                                    if (container.tagName === 'BODY' || container.classList.contains('stApp')) break;
                                }
                            }
                        });
                    } else {
                        setTimeout(rotateXAxisLabels, 100);
                    }
                }
                // Try immediately and also on load, with multiple retries
                setTimeout(rotateXAxisLabels, 100);
                setTimeout(rotateXAxisLabels, 500);
                setTimeout(rotateXAxisLabels, 1000);
                window.addEventListener('load', rotateXAxisLabels);
                // Also try after a longer delay
                setTimeout(rotateXAxisLabels, 2000);
            })();
            </script>
            """
            # Insert before closing body tag
            if '</body>' in content:
                content = content.replace('</body>', js_injection + '</body>')
            else:
                content += js_injection
        
        return content
    else:
        return f"<p style='color: red;'>File not found: {file_path}</p>"

def main():
    # Title (centered)
    st.markdown("<h1 style='text-align: center;'>📊 Author Identification Visualizations</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Create tabs for different visualizations
    tab1, tab2, tab3 = st.tabs([
        "📚 Algazi Book Similarity",
        "📚 Krakash Book Similarity", 
        "📈 Author Evaluation"
    ])
    
    # Tab 1: Algazi Book Similarity Heatmap (larger)
    with tab1:
        st.header("Algazi Book Similarity Heatmap")
        st.markdown("""
        **Interactive heatmap showing similarity between Algazi books.**
        
        This visualization displays cosine similarity scores (median of 5 chunk comparisons) 
        between pairs of books from the Algazi collection. Higher similarity scores (closer to 1.0) 
        indicate more similar writing styles.
        """)
        
        if ALGAZI_HTML.exists():
            html_content = load_html_file(ALGAZI_HTML)
            # Center the figure and make it larger
            st.markdown("""
            <div style="display: flex; justify-content: center; align-items: center; width: 100%;">
            """, unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 10, 1])
            with col2:
                st.components.v1.html(html_content, height=1000, scrolling=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.error(f"File not found: {ALGAZI_HTML}")
            st.info("Please run the inference script to generate this visualization.")
    
    # Tab 2: Krakash Book Similarity Heatmap (with fixed labels)
    with tab2:
        st.header("Krakash Book Similarity Heatmap")
        st.markdown("""
        **Interactive heatmap showing similarity between Krakash books.**
        
        This visualization displays cosine similarity scores (median of 5 chunk comparisons) 
        between pairs of books from the Krakash collection. Higher similarity scores (closer to 1.0) 
        indicate more similar writing styles.
        """)
        
        if KARKASH_HTML.exists():
            try:
                html_content = load_html_file(KARKASH_HTML, modify_karkash_labels=True)
                # Center the figure with extra padding for labels
                col1, col2, col3 = st.columns([1, 10, 1])
                with col2:
                    st.components.v1.html(html_content, height=900, scrolling=True)
            except Exception as e:
                st.error(f"Error loading Krakash visualization: {e}")
                st.info("Trying to load without modifications...")
                try:
                    html_content = load_html_file(KARKASH_HTML, modify_karkash_labels=False)
                    col1, col2, col3 = st.columns([1, 10, 1])
                    with col2:
                        st.components.v1.html(html_content, height=900, scrolling=True)
                except Exception as e2:
                    st.error(f"Error: {e2}")
        else:
            st.error(f"File not found: {KARKASH_HTML}")
            st.info("Please run the inference script to generate this visualization.")
    
    # Tab 3: Author Evaluation (centered)
    with tab3:
        st.header("Author Chunk Evaluation: Index vs Median Similarity")
        st.markdown("""
        **Scatter plot showing similarity distributions for author identification evaluation.**
        
        This visualization compares:
        - **Green dots**: Positive pairs (same author, different books)
        - **Red dots**: Negative pairs (different authors)
        
        Each point represents a book pair comparison, with the y-axis showing median similarity 
        across chunk comparisons. The black dashed line at 0.5 represents the classification threshold.
        """)
        
        if AUTHOR_EVAL_HTML.exists():
            html_content = load_html_file(AUTHOR_EVAL_HTML)
            # Center the figure
            st.markdown("""
            <div style="display: flex; justify-content: center; align-items: center; width: 100%;">
            """, unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 10, 1])
            with col2:
                st.components.v1.html(html_content, height=800, scrolling=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.error(f"File not found: {AUTHOR_EVAL_HTML}")
            st.info("Please run the evaluation script to generate this visualization.")

if __name__ == "__main__":
    main()

