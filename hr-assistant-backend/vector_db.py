from typing import Dict, List, Optional
import numpy as np
import os
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

class VectorDBService:
    @staticmethod
    def search_similar_profiles(
        employee_data: Dict,
        target_role: Optional[str] = None,
        target_grade: Optional[str] = None,
        target_department: Optional[str] = None,
        target_job_family: Optional[str] = None
    ) -> List[Dict]:
        search_client = SearchClient(
            endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
            index_name="azureblob-index",
            credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_QUERY_KEY"))
        )

        # Build search filters based on targets
        filters = []
        if target_role:
            filters.append(f"ROLE eq '{target_role}'")
        if target_grade:
            filters.append(f"GRADE eq '{target_grade}'")
        if target_department:
            filters.append(f"DEPARTMENT eq '{target_department}'")
        if target_job_family:
            filters.append(f"JOB_FAMILY eq '{target_job_family}'")

        filter_expr = " and ".join(filters) if filters else None

        # Search for similar profiles
        results = search_client.search(
            search_text="*",
            filter=filter_expr,
            select=["*"],
            top=5
        )

        return [dict(result) for result in results]