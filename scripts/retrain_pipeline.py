# scripts/retrain_pipeline.py

from datetime import datetime
from scripts.main_pipeline import main  # if main_pipeline.py is refactored into a callable main()

if __name__ == "__main__":
    print(f"Retraining pipeline started at {datetime.now()}")
    # Run main pipeline
    main()
    print(f"Retraining pipeline completed at {datetime.now()}")
