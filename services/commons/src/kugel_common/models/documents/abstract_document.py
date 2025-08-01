# Copyright 2025 masa@kugel
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from datetime import datetime
from typing import Optional
from kugel_common.models.documents.base_document_model import BaseDocumentModel

class AbstractDocument(BaseDocumentModel):
    """
    Abstract base document model for database entities.
    
    This class extends BaseDocumentModel to provide common fields needed for database
    persistence and management, such as shard key, timestamps for creation and updates,
    and etag for concurrency control. All persistent document models in the system
    should extend this class.
    """
    shard_key: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    etag: Optional[str] = None
