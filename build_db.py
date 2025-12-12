#!/usr/bin/env python3
"""
Build script to pre-build the SQLite database for Vercel deployment.
Run this before deploying to Vercel to include the pre-built database.
"""

import os
import sys

def main():
    print("Building database for Vercel deployment...")
    
    # Create database directory
    os.makedirs("database", exist_ok=True)
    
    # Set the database path
    os.environ["WORKFLOW_DB_PATH"] = "database/workflows.db"
    
    # Import and initialize database
    from workflow_db import WorkflowDatabase
    
    db = WorkflowDatabase("database/workflows.db")
    
    # Force reindex all workflows
    print("Indexing all workflows...")
    stats = db.index_all_workflows(force_reindex=True)
    
    print(f"Database built successfully!")
    print(f"  - Processed: {stats['processed']}")
    print(f"  - Skipped: {stats['skipped']}")
    print(f"  - Errors: {stats['errors']}")
    
    # Get final stats
    final_stats = db.get_stats()
    print(f"  - Total workflows: {final_stats['total']}")
    
    db_size = os.path.getsize("database/workflows.db")
    print(f"  - Database size: {db_size / 1024:.1f} KB")
    
    print("\nDatabase ready for Vercel deployment!")
    print("The database will be included in your deployment.")

if __name__ == "__main__":
    main()
