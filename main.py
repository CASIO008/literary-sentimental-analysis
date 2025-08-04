from scripts.analyze_sentiment import AzureTextAnalyzer
def main():
    analyzer = AzureTextAnalyzer()
    
    filename = "dom_casmurro.txt"
    with open(f"texts/{filename}", "r", encoding="utf-8") as f:
        text = f.read()

    result = analyzer.analyze_text(text)
    analyzer.print_summary(result)
    analyzer.save_results(result, "dom_casmurro_analysis.json")

if __name__ == "__main__":
    main()