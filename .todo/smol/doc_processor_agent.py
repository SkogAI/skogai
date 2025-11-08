#!/usr/bin/env python3
"""
📄 Document Processor Agent - SOLVES THE 12-14 HOUR WEEKEND PROBLEM

This agent automatically categorizes, classifies, and summarizes documentation
and chat logs. Designed to save Skogix 12-14 hours every weekend.

Usage:
    python doc_processor_agent.py process /path/to/documents
    python doc_processor_agent.py web  # Web UI for drag-and-drop
"""

import json
import re
from pathlib import Path
from datetime import datetime

from smolagents import CodeAgent, LiteLLMModel, tool
from smolagents import FinalAnswerTool, PythonInterpreterTool


@tool
def read_file_content(file_path: str, max_chars: int = 10000) -> str:
    """Read the content of a file safely

    Args:
        file_path: Path to the file to read
        max_chars: Maximum characters to read (default 10000)
    """
    try:
        path = Path(file_path)
        if not path.exists():
            return f"❌ File not found: {file_path}"

        # Try UTF-8 first, fallback to latin-1
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read(max_chars)
        except UnicodeDecodeError:
            with open(path, "r", encoding="latin-1") as f:
                content = f.read(max_chars)

        if len(content) == max_chars:
            content += "\n... [truncated for length]"

        return f"📄 Content of {path.name}:\n{content}"

    except Exception as e:
        return f"❌ Error reading file: {str(e)}"


@tool
def batch_process_files(
    directory_path: str, file_pattern: str = "*.md", max_files: int = 50
) -> str:
    """Process multiple files in batches to avoid overwhelming the agent

    Args:
        directory_path: Directory to scan
        file_pattern: Pattern to match files (default *.md)
        max_files: Maximum files to process in one batch
    """
    try:
        path = Path(directory_path)
        if not path.exists():
            return f"❌ Directory not found: {directory_path}"

        # Find matching files
        files = list(path.glob(file_pattern))[:max_files]

        if not files:
            return f"❌ No files matching {file_pattern} found in {directory_path}"

        result = "📁 BATCH PROCESSING REPORT\n"
        result += f"Directory: {directory_path}\n"
        result += f"Pattern: {file_pattern}\n"
        result += (
            f"Files processed: {len(files)}/{len(list(path.glob(file_pattern)))}\n"
        )
        result += "=" * 50 + "\n\n"

        summaries = []
        for file_path in files:
            try:
                # Quick analysis without reading full content
                stat = file_path.stat()
                size = stat.st_size

                # Read first few lines for quick categorization
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        first_lines = [f.readline().strip() for _ in range(5)]
                except UnicodeDecodeError:
                    with open(file_path, "r", encoding="latin-1") as f:
                        first_lines = [f.readline().strip() for _ in range(5)]

                preview = " | ".join(line for line in first_lines if line)[:100]

                summaries.append(
                    {"name": file_path.name, "size": size, "preview": preview}
                )

            except Exception as e:
                summaries.append(
                    {"name": file_path.name, "size": 0, "preview": f"Error: {str(e)}"}
                )

        # Sort by size (largest first)
        summaries.sort(key=lambda x: x["size"], reverse=True)

        result += "📊 FILE SUMMARY:\n"
        for summary in summaries:
            result += f"• {summary['name']} ({summary['size']:,} bytes)\n"
            result += f"  Preview: {summary['preview']}\n\n"

        result += "\n🎯 Use read_file_content() to examine specific files\n"
        result += "🎯 Use categorize_single_file() for detailed analysis\n"

        return result

    except Exception as e:
        return f"❌ Error processing batch: {str(e)}"


@tool
def process_directory(directory_path: str) -> str:
    """Process all documents in a directory and categorize them

    Args:
        directory_path: Path to directory containing documents to process
    """
    try:
        path = Path(directory_path)
        if not path.exists():
            return f"❌ Directory not found: {directory_path}"

        # Find all text-based files
        text_extensions = {
            ".txt",
            ".md",
            ".log",
            ".json",
            ".csv",
            ".py",
            ".js",
            ".html",
            ".xml",
        }
        files = []

        for file_path in path.rglob("*"):
            if file_path.is_file() and file_path.suffix.lower() in text_extensions:
                files.append(str(file_path))

        if not files:
            return f"❌ No processable files found in {directory_path}"

        result = "📄 DOCUMENT PROCESSING REPORT\n"
        result += f"Directory: {directory_path}\n"
        result += f"Files found: {len(files)}\n"
        result += f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        result += "=" * 60 + "\n\n"

        # Group files by type
        by_type = {}
        for file_path in files:
            ext = Path(file_path).suffix.lower()
            if ext not in by_type:
                by_type[ext] = []
            by_type[ext].append(file_path)

        result += "📊 FILES BY TYPE:\n"
        for ext, file_list in sorted(by_type.items()):
            result += f"  {ext}: {len(file_list)} files\n"

        result += "\n🎯 Ready for detailed processing with categorize_documents tool\n"
        result += (
            f"File list: {json.dumps(files[:20])}{'...' if len(files) > 20 else ''}\n"
        )

        return result

    except Exception as e:
        return f"❌ Error processing directory: {str(e)}"


@tool
def categorize_single_file(file_path: str) -> str:
    """Categorize and analyze a single document file

    Args:
        file_path: Path to the file to categorize
    """
    try:
        path = Path(file_path)
        if not path.exists():
            return f"❌ File not found: {file_path}"

        # Read file content
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
        except UnicodeDecodeError:
            with open(path, "r", encoding="latin-1") as f:
                content = f.read()

        # Basic analysis
        lines = content.split("\n")
        words = content.split()

        # Detect file type patterns
        file_type = "unknown"
        category = "miscellaneous"
        importance = "medium"

        # Chat log detection
        if re.search(r"\[\d{4}-\d{2}-\d{2}.*?\]|<.*?>", content[:1000]):
            file_type = "chat_log"
            category = "communication"

        # Code detection
        elif path.suffix in [".py", ".js", ".html", ".css"]:
            file_type = "code"
            category = "development"

        # Documentation detection
        elif path.suffix in [".md", ".txt"] and any(
            word in content.lower()[:500]
            for word in ["readme", "documentation", "guide", "manual"]
        ):
            file_type = "documentation"
            category = "reference"

        # Log file detection
        elif "error" in content.lower()[:1000] or "exception" in content.lower()[:1000]:
            file_type = "error_log"
            category = "troubleshooting"
            importance = "high"

        # Data file detection
        elif path.suffix in [".csv", ".json"] or "," in content[:200]:
            file_type = "data"
            category = "datasets"

        # Extract key information
        key_terms = []
        # Simple keyword extraction
        common_words = {
            "the",
            "and",
            "or",
            "but",
            "in",
            "on",
            "at",
            "to",
            "for",
            "of",
            "with",
            "by",
            "is",
            "are",
            "was",
            "were",
            "be",
            "been",
            "have",
            "has",
            "had",
            "do",
            "does",
            "did",
            "will",
            "would",
            "could",
            "should",
            "may",
            "might",
            "can",
            "a",
            "an",
        }
        word_freq = {}
        for word in words:
            clean_word = re.sub(r"[^\w]", "", word.lower())
            if len(clean_word) > 3 and clean_word not in common_words:
                word_freq[clean_word] = word_freq.get(clean_word, 0) + 1

        # Top keywords
        key_terms = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]

        result = f"📄 FILE ANALYSIS: {path.name}\n"
        result += "=" * 50 + "\n"
        result += f"Path: {file_path}\n"
        result += f"Size: {len(content):,} characters\n"
        result += f"Lines: {len(lines):,}\n"
        result += f"Words: {len(words):,}\n"
        result += f"Type: {file_type}\n"
        result += f"Category: {category}\n"
        result += f"Importance: {importance}\n\n"

        result += "🔍 KEY TERMS:\n"
        for term, freq in key_terms[:5]:
            result += f"  • {term} ({freq}x)\n"

        # Generate summary
        first_lines = "\n".join(lines[:5])
        result += f"\n📋 CONTENT PREVIEW:\n{first_lines[:200]}{'...' if len(first_lines) > 200 else ''}\n"

        return result

    except Exception as e:
        return f"❌ Error analyzing file: {str(e)}"


@tool
def extract_chat_summaries(log_file: str, time_window: str = "daily") -> str:
    """Extract and summarize chat conversations from log files

    Args:
        log_file: Path to chat log file
        time_window: Grouping window (hourly, daily, weekly)
    """
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Parse different chat log formats
        conversations = []

        # Discord/Slack format: [timestamp] username: message
        discord_pattern = r"\[(\d{4}-\d{2}-\d{2}.*?)\]\s*([^:]+):\s*(.+)"
        discord_matches = re.findall(discord_pattern, content, re.MULTILINE)

        if discord_matches:
            for timestamp, user, message in discord_matches:
                conversations.append(
                    {
                        "timestamp": timestamp,
                        "user": user.strip(),
                        "message": message.strip(),
                    }
                )

        # IRC format: <username> message
        irc_pattern = r"<([^>]+)>\s*(.+)"
        irc_matches = re.findall(irc_pattern, content, re.MULTILINE)

        if irc_matches and not discord_matches:
            for user, message in irc_matches:
                conversations.append(
                    {
                        "timestamp": "unknown",
                        "user": user.strip(),
                        "message": message.strip(),
                    }
                )

        if not conversations:
            return f"❌ No chat patterns detected in {log_file}"

        # Group conversations
        summary = f"💬 CHAT LOG SUMMARY: {Path(log_file).name}\n"
        summary += "=" * 50 + "\n"
        summary += f"Total messages: {len(conversations)}\n"
        summary += f"Time window: {time_window}\n\n"

        # Count by user
        user_counts = {}
        for conv in conversations:
            user = conv["user"]
            user_counts[user] = user_counts.get(user, 0) + 1

        summary += "👥 PARTICIPANTS:\n"
        for user, count in sorted(
            user_counts.items(), key=lambda x: x[1], reverse=True
        ):
            summary += f"  • {user}: {count} messages\n"

        # Extract key topics (simple keyword analysis)
        all_messages = " ".join([c["message"] for c in conversations])
        words = re.findall(r"\b\w{4,}\b", all_messages.lower())
        word_freq = {}
        for word in words:
            if word not in {
                "that",
                "this",
                "with",
                "have",
                "will",
                "they",
                "were",
                "been",
                "from",
                "what",
                "when",
                "where",
                "about",
            }:
                word_freq[word] = word_freq.get(word, 0) + 1

        top_topics = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]

        summary += "\n🏷️ KEY TOPICS:\n"
        for topic, freq in top_topics[:5]:
            summary += f"  • {topic} ({freq}x)\n"

        # Sample recent conversations
        recent_convs = conversations[-5:] if len(conversations) > 5 else conversations
        summary += "\n📝 RECENT MESSAGES:\n"
        for conv in recent_convs:
            user = conv["user"][:15]
            message = conv["message"][:60]
            summary += (
                f"  {user}: {message}{'...' if len(conv['message']) > 60 else ''}\n"
            )

        return summary

    except Exception as e:
        return f"❌ Error processing chat log: {str(e)}"


@tool
def generate_processing_report(directory_path: str) -> str:
    """Generate comprehensive processing report for all documents

    Args:
        directory_path: Directory that was processed
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"doc_processing_report_{timestamp}.md"

    report = f"""# Document Processing Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Directory: {directory_path}

## Summary
This report was generated automatically by the Document Processor Agent to save manual categorization time.

## Processing Results
- **Total files processed**: [To be filled by agent]
- **Categories identified**: [To be filled by agent]
- **High priority items**: [To be filled by agent]
- **Recommended actions**: [To be filled by agent]

## File Categories
### Communication (Chat logs, emails)
### Development (Code, scripts)
### Documentation (Guides, references)
### Data (CSV, JSON, datasets)
### Troubleshooting (Error logs, debug info)
### Miscellaneous (Other files)

## Next Steps
1. Review high priority items first
2. Archive processed files
3. Update project documentation
4. Schedule next processing run

---
*Generated by Document Processor Agent - Saving you 12-14 hours of manual work*
"""

    try:
        with open(report_file, "w") as f:
            f.write(report)
        return f"✅ Report saved to {report_file}\n\n{report}"
    except Exception as e:
        return f"❌ Error saving report: {str(e)}\n\n{report}"


def create_doc_processor():
    """Create the document processing agent"""

    # Use local model for privacy with documents
    try:
        model = LiteLLMModel(
            model_id="ollama_chat/qwen2.5-coder",  # Good for text processing
            api_base="http://localhost:11434",
            num_ctx=8192,
            temperature=0.2,  # Low for consistent categorization
        )
    except:
        # Fallback
        model = LiteLLMModel(
            model_id="ollama_chat/llama3.2",
            api_base="http://localhost:11434",
            num_ctx=4096,
            temperature=0.2,
        )

    agent = CodeAgent(
        tools=[
            read_file_content,  # Safe file reading
            batch_process_files,  # Handle large numbers of files
            process_directory,  # Scan directories
            categorize_single_file,  # Analyze individual files
            extract_chat_summaries,  # Parse chat logs
            generate_processing_report,  # Create reports
            PythonInterpreterTool(),  # For data processing
            FinalAnswerTool(),  # Results
        ],
        model=model,
        name="Document_Processor",
        description="Automated document categorization and chat log processing to save manual weekend work",
        max_steps=15,  # Increased for batch processing
        stream_outputs=True,
        additional_authorized_imports=[
            "pathlib",
            "json",
            "re",
            "datetime",
            "os",
            "glob",
        ],
    )

    return agent


def process_documents_cli(directory_path: str):
    """CLI interface for document processing"""
    print(f"📄 Processing documents in: {directory_path}")

    agent = create_doc_processor()

    task = f"""
Process all documents in the directory '{directory_path}'. I need:

1. Scan the directory and identify all processable files
2. Categorize each file by type and importance
3. For any chat logs, extract key conversation summaries
4. Generate a comprehensive report
5. Save the report to a file

This should automate the manual categorization work that takes 12-14 hours every weekend.
"""

    try:
        result = agent.run(task)
        print("\n" + "=" * 60)
        print("✅ PROCESSING COMPLETE!")
        print("=" * 60)
        print(result)
    except Exception as e:
        print(f"❌ Processing failed: {e}")


def deploy_web_ui():
    """Deploy web interface for document processing"""
    from smolagents import GradioUI

    print("🌐 Starting Document Processor Web UI...")
    agent = create_doc_processor()

    ui = GradioUI(
        agent,
        file_upload_folder="./doc_processing",
        # share=True,
        # server_name="0.0.0.0",
        # server_port=7870,
    )

    print("📄 Document Processor: http://localhost:7870")
    print("💡 Drag and drop files or specify directory paths")
    ui.launch()


def create_documentation_professor():
    """Create the Documentation Professor agent - specialized for helping the Librarian"""

    # Use local model for privacy with documents
    try:
        model = LiteLLMModel(
            model_id="ollama_chat/qwen2.5-coder",  # Good for text processing
            api_base="http://localhost:11434",
            num_ctx=8192,
            temperature=0.1,  # Very low for consistent documentation
        )
    except:
        # Fallback
        model = LiteLLMModel(
            model_id="ollama_chat/llama3.2",
            api_base="http://localhost:11434",
            num_ctx=4096,
            temperature=0.1,
        )

    agent = CodeAgent(
        tools=[
            read_file_content,  # Safe file reading
            batch_process_files,  # Handle large numbers of files
            process_directory,  # Scan directories
            categorize_single_file,  # Analyze individual files
            extract_chat_summaries,  # Parse chat logs
            generate_processing_report,  # Create reports
            PythonInterpreterTool(),  # For data processing
            FinalAnswerTool(),  # Results
        ],
        model=model,
        name="Documentation_Professor",
        description="Specialized documentation processing agent that helps the SkogAI Librarian manage massive text volumes and knowledge organization",
        max_steps=20,  # More steps for complex analysis
        stream_outputs=True,
        additional_authorized_imports=[
            "pathlib",
            "json",
            "re",
            "datetime",
            "os",
            "docx",
            "xml.etree.ElementTree",
            "glob",
        ],
    )

    return agent


def deploy_documentation_professor_cli(directory_path: str):
    """CLI interface for Documentation Professor processing"""
    print(f"📚 Documentation Professor processing: {directory_path}")

    agent = create_documentation_professor()

    task = f"""
I am the Documentation Professor, specialized in helping the SkogAI Librarian process large volumes of text.

For the directory '{directory_path}':

STEP 1: Use batch_process_files to get an overview of all markdown files
- Start with pattern "*.md" and max_files=50 to avoid overwhelming
- Review file sizes and types

STEP 2: Use read_file_content selectively for key documents
- Focus on largest or most important files first
- Extract key concepts and themes

STEP 3: Perform taxonomic classification:
- Technical documentation (code, APIs, specifications)
- Governance documents (policies, decisions, votes)
- Planning materials (roadmaps, proposals, strategies)
- Communication logs (meetings, discussions)
- Reference materials (guides, tutorials)

STEP 4: Generate executive summary for the Librarian:
- Key themes across all documents
- Important decisions or technical information
- Cross-references between related topics
- Recommended archival structure

Use the batch processing approach to handle large numbers of files efficiently.
"""

    try:
        result = agent.run(task)
        print("\n" + "=" * 60)
        print("✅ DOCUMENTATION PROFESSOR ANALYSIS COMPLETE!")
        print("=" * 60)
        print(result)
    except Exception as e:
        print(f"❌ Analysis failed: {e}")


def deploy_professor_web_ui():
    """Deploy web interface for Documentation Professor"""
    from smolagents import GradioUI

    print("🌐 Starting Documentation Professor Web UI...")
    agent = create_documentation_professor()

    ui = GradioUI(
        agent,
        file_upload_folder="./professor_processing",
        share=False,
        server_name="0.0.0.0",
        server_port=7875,
    )

    print("📚 Documentation Professor: http://localhost:7875")
    print("💡 Specialized for Librarian support and knowledge processing")
    ui.launch()


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python doc_processor_agent.py process /path/to/documents")
        print("  python doc_processor_agent.py web")
        print("  python doc_processor_agent.py professor /path/to/documents")
        print("  python doc_processor_agent.py professor-web")
        sys.exit(1)

    command = sys.argv[1]

    if command == "process" and len(sys.argv) > 2:
        directory_path = sys.argv[2]
        process_documents_cli(directory_path)
    elif command == "web":
        deploy_web_ui()
    elif command == "professor" and len(sys.argv) > 2:
        directory_path = sys.argv[2]
        deploy_documentation_professor_cli(directory_path)
    elif command == "professor-web":
        deploy_professor_web_ui()
    else:
        print(
            "❌ Invalid command. Use 'process <directory>', 'web', 'professor <directory>', or 'professor-web'"
        )
