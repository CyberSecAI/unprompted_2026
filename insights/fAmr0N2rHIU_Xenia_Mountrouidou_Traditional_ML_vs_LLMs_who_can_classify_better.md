# Traditional ML vs LLMs: who can classify better?

**Video ID:** fAmr0N2rHIU

**YouTube Link:** https://www.youtube.com/watch?v=fAmr0N2rHIU

**Transcript:** [View Transcript](../transcripts/fAmr0N2rHIU_Xenia%20Mountrouidou%20-%20Traditional%20ML%20vs%20LLMs%EF%BC%9A%20who%20can%20classify%20better%EF%BC%9F%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Xenia Mountrouidou (Dr. X) from Expel evaluates the performance of traditional ML (e.g., XGBoost) against LLMs for classifying security threats like botnets and phishing.

## Key Takeaway
Traditional ML models remain the gold standard for accuracy in structured security data, though LLMs offer superior zero-shot capabilities for unstructured text.

# Insights

## Predictive vs. Generative Paradigms
- Traditional predictive models are specifically designed to find and enforce boundaries in well-labeled, structured security datasets.
- Generative models are being increasingly tested for classification, but they lack the native mathematical focus required for high-precision boundary detection.
- In head-to-head trials using networking data, traditional ML models consistently outperformed LLMs in both precision and recall metrics.

## The Power of Zero-Shot
- LLMs provide "zero-shot" classification, allowing security teams to categorize data via natural language prompts without any prior training.
- This represents a major operational shift, potentially removing the need for massive, manually labeled datasets for every new vulnerability class.
- While promising, zero-shot performance currently lags behind specialized, task-specific models for complex, non-textual data like packet captures.

## Challenges with Non-Textual Data
- Networking data (PCAPs) is fundamentally difficult for LLMs because it is not natural language and cannot be easily tokenized.
- Effective LLM-based classification of packets requires extensive feature engineering (protocol, payload, timelines) to translate data into a model-friendly format.
- Relying on LLMs for structured system logs often leads to lower sensitivity and more frequent misclassifications compared to traditional algorithms.

## Ensemble Model Architectures
- The most effective classification systems utilize an "ensemble" approach, combining traditional ML with the reasoning flexibility of LLMs.
- A "router" architecture uses fast models like XGBoost for initial triage, escalating only the most ambiguous samples to an LLM.
- Combining these methodologies produces higher overall efficacy than using either traditional ML or generative AI as a standalone solution.

## Precision and Recall Stability
- Traditional ML models (like XGBoost) provide stable, repeatable results that are essential for high-fidelity security alerts.
- LLMs exhibit higher variance and can produce wildly different classification results based on minor changes to the input prompt.
- Maintaining high precision in production environments requires the deterministic boundary enforcement that traditional models provide.

## Classification Nuances
- Modern security requires multiclass classification to handle complex states like "possibly benign" or "suspicious but low-impact."
- Traditional models are more adept at identifying these categorical nuances in telemetry data than general-purpose generative models.
- Specialized security embeddings can help LLMs close the gap, but they do not yet consistently beat generalist models with traditional feature engineering.

## Phishing and Natural Language
- LLMs demonstrate their highest security value when classifying unstructured natural language threats, such as sophisticated phishing or social engineering.
- For textual data, LLMs can understand the subtle context and intent that traditional keyword-based or simple ML models frequently miss.
- Email security is the primary domain where LLMs are reaching parity with, or exceeding, the performance of traditional ML classifiers.

## Cost and Latency Constraints
- Generative models are significantly more expensive and have much higher latency per sample than traditional lightweight ML algorithms.
- High-latency classification is unfeasible for real-time monitoring of millions of daily network packets or system events.
- Organizations must balance the reasoning power of LLMs with the economic and temporal efficiency of traditional predictive modeling.
