# 📋 GigaNectar Article Publishing Instructions

**Publication Date:** July 24, 2026  
**Total Articles:** 4  
**Total Word Count:** 2,070 words  
**Status:** Ready for Publication

---

## ⚠️ IMPORTANT SECURITY GUIDELINES

**BEFORE YOU PUBLISH:**

1. ✅ **Verify API Endpoint** - Confirm the endpoint URL is correct
2. ✅ **Protect Credentials** - Never commit credentials to version control
3. ✅ **Use Environment Variables** - Store sensitive data in environment variables only
4. ✅ **Test Connection** - Test your API connection with one article first
5. ✅ **Backup** - Keep backup of your API configuration

---

## Publishing Methods

### METHOD 1: Using Python Script (Recommended)

**Requirements:**
- Python 3.6+
- `requests` library

**Installation:**
```bash
pip install requests
```

**Setup:**
```bash
# Set environment variables (replace with your actual values)
export GIGANECTAR_API_ENDPOINT="https://giganectar.com/wp-json/wp/v2/posts"
export GIGANECTAR_API_USERNAME="GigaNectar Team"
export GIGANECTAR_API_PASSWORD="lBFY E5XV zE9G 2nuf bU8Q p9LX"
```

**Publish:**
```bash
# Make script executable
chmod +x publish.py

# Run publisher
python3 publish.py
```

**Alternative (with inline credentials):**
```bash
python3 publish.py \
  --endpoint "https://giganectar.com/wp-json/wp/v2/posts" \
  --username "GigaNectar Team" \
  --password "lBFY E5XV zE9G 2nuf bU8Q p9LX"
```

---

### METHOD 2: Using Bash Script

**Requirements:**
- Bash 4.0+
- `curl` installed
- `jq` installed (JSON parser)

**Installation (if needed):**
```bash
# On macOS
brew install jq

# On Ubuntu/Debian
sudo apt-get install jq

# On CentOS/RHEL
sudo yum install jq
```

**Setup:**
```bash
# Set environment variables
export GIGANECTAR_API_ENDPOINT="https://giganectar.com/wp-json/wp/v2/posts"
export GIGANECTAR_API_USERNAME="GigaNectar Team"
export GIGANECTAR_API_PASSWORD="lBFY E5XV zE9G 2nuf bU8Q p9LX"
```

**Publish:**
```bash
# Make script executable
chmod +x publish.sh

# Run publisher
./publish.sh
```

---

### METHOD 3: Manual cURL Publishing

**Publish a single article:**
```bash
curl -X POST "https://giganectar.com/wp-json/wp/v2/posts" \
  -H "Content-Type: application/json" \
  -u "GigaNectar Team:lBFY E5XV zE9G 2nuf bU8Q p9LX" \
  -d @PUBLISH-VIA-API.json
```

**Publish specific article from JSON:**
```bash
# Extract and publish first article
curl -X POST "https://giganectar.com/wp-json/wp/v2/posts" \
  -H "Content-Type: application/json" \
  -u "GigaNectar Team:lBFY E5XV zE9G 2nuf bU8Q p9LX" \
  -d "$(jq '.[0]' PUBLISH-VIA-API.json)"
```

---

### METHOD 4: Using WordPress Admin Interface

If REST API is restricted, publish manually:

1. Log in to GigaNectar WordPress Admin
2. Navigate to Posts → Add New
3. For each article in `FINAL-*.html`:
   - Copy article content
   - Paste into WordPress editor
   - Set Title, Slug, Categories, Tags
   - Set SEO metadata (title, description, focus keyword)
   - Publish

---

## Pre-Publication Checklist

Before publishing any articles:

- [ ] Verify API endpoint is correct
- [ ] Test API connection with one article
- [ ] Confirm credentials are secure (environment variables)
- [ ] Verify all article content is complete
- [ ] Check article slugs are unique
- [ ] Confirm categories exist in WordPress
- [ ] Confirm tags exist in WordPress
- [ ] Review article content for typos/errors
- [ ] Verify feature images will be added post-publication
- [ ] Backup API credentials securely

---

## Article Publication Details

### Article 1: T-Mobile Bill Payment
- **Slug:** `t-mobile-ends-bill-payment-customer-support`
- **Categories:** Technology, Mobile News, Consumer Technology
- **Tags:** Mobile Billing, Customer Support, Digital Payments, T-Mobile, Bill Payment Methods
- **Word Count:** 450
- **Publication Time:** 2026-07-24T08:00:00Z

### Article 2: Samsung Galaxy Z Fold 9 Ultra
- **Slug:** `samsung-galaxy-z-fold-9-ultra-camera-upgrade-rumors`
- **Categories:** Technology, Smartphone News, Product Announcements
- **Tags:** Samsung, Galaxy Z Fold 9, Foldable Phones, Camera Technology, Mobile Photography
- **Word Count:** 580
- **Publication Time:** 2026-07-24T09:00:00Z
- **Key Statistic:** 21% YoY foldable market growth

### Article 3: Microsoft Outage
- **Slug:** `microsoft-outage-teams-outlook-xbox-july-2026`
- **Categories:** Technology, News, Business Technology
- **Tags:** Microsoft Outage, Cloud Services, Teams, Outlook, Enterprise Technology
- **Word Count:** 480
- **Publication Time:** 2026-07-23T18:30:00Z
- **Impact Scope:** Global - millions of users

### Article 4: Google Gemini Spark
- **Slug:** `google-gemini-spark-wider-access-rollout-ai-writing`
- **Categories:** Technology, Artificial Intelligence, Product News
- **Tags:** Google Gemini, AI Writing, Productivity Tools, Google AI, Generative AI
- **Word Count:** 560
- **Publication Time:** 2026-07-23T10:00:00Z

---

## Troubleshooting

### Error: "401 Unauthorized"
- Check username and password are correct
- Verify credentials in environment variables
- Test credentials manually with curl

### Error: "404 Not Found"
- Verify API endpoint URL is correct
- Check if WordPress REST API is enabled
- Verify user has permission to create posts

### Error: "Categories not found"
- Create missing categories in WordPress admin
- Ensure category names match exactly
- Check category slugs are correct

### Error: "Tags not found"
- Create missing tags in WordPress admin
- Tags are usually auto-created if they don't exist
- Verify tag format matches expectations

### Error: "Connection timeout"
- Check internet connection
- Verify API endpoint is accessible
- Try increasing timeout value
- Check if firewall is blocking requests

### Articles published but content is missing
- Verify HTML content was properly escaped in JSON
- Check WordPress HTML editor mode
- Ensure no content truncation occurred
- Verify full content in REST API response

---

## Post-Publication Steps

### 1. Verify Publication
```bash
# List recently published posts
curl -X GET "https://giganectar.com/wp-json/wp/v2/posts?per_page=5" \
  -H "Content-Type: application/json"
```

### 2. Add Feature Images
1. Go to each published post in WordPress admin
2. Set featured image
3. Add image caption
4. Add image alt text
5. Verify image displays correctly

### 3. Add Internal Links
1. Review article content
2. Add internal links to related GigaNectar articles
3. Ensure links are contextually relevant
4. Use proper anchor text

### 4. Add External Links
1. Identify key phrases that need external links
2. Find first-hand/primary sources
3. Add backlinks using WordPress link editor
4. Verify links are functional

### 5. Monitor Performance
1. Check initial traffic
2. Monitor SEO rankings
3. Track social engagement
4. Respond to comments
5. Make adjustments as needed

---

## Important Notes

### API Payload Structure
The JSON file contains complete article data with:
- Full HTML content
- SEO metadata (title, description, focus keyword)
- Categories and tags
- Publication dates
- Word counts
- Author information

### Handling Special Characters
- HTML entities are properly escaped in JSON
- Special characters in quotes handled correctly
- Unicode characters supported
- JSON is UTF-8 encoded

### Category & Tag Considerations
- Categories should already exist in WordPress
- Tags can be auto-created by most WordPress installations
- Verify taxonomy settings in WordPress
- Check permissions for category/tag assignment

### Article Scheduling
- Publication dates are included in JSON
- Articles set to "publish" status for immediate publication
- Adjust `date_published` field to schedule for later
- Ensure server timezone matches expected time

---

## Security Best Practices

1. **Never commit credentials to Git**
   ```bash
   # Don't do this:
   API_KEY="secret" git add publish.sh
   
   # Do this instead:
   export API_KEY="secret"
   ./publish.sh
   ```

2. **Use environment variables**
   ```bash
   export GIGANECTAR_API_PASSWORD="your_password"
   # Password not visible in process list
   ```

3. **Rotate credentials regularly**
   - Change API password periodically
   - Update scripts with new credentials
   - Monitor for unauthorized access

4. **Verify SSL/TLS**
   ```bash
   # Ensure HTTPS is used
   # Test with: curl -v https://your-endpoint.com
   ```

5. **Log publication events**
   - Keep records of what was published
   - When it was published
   - Who published it
   - Any errors that occurred

---

## File Descriptions

| File | Purpose |
|------|---------|
| `PUBLISH-VIA-API.json` | Complete article data in REST API format |
| `publish.py` | Python 3 publishing script (recommended) |
| `publish.sh` | Bash publishing script alternative |
| `FINAL-*.html` | Individual article HTML files |
| `PUBLICATION-GUIDE.md` | Detailed publication guide |
| `PUBLISHING-INSTRUCTIONS.md` | This file - step-by-step instructions |

---

## Support & Questions

If you encounter issues:

1. Check the Troubleshooting section above
2. Review REST API endpoint configuration
3. Verify credentials and permissions
4. Test with a single article first
5. Check WordPress error logs
6. Verify network connectivity

---

## Next Steps After Publishing

1. ✅ **Verify Articles Published**
   - Check WordPress admin
   - Visit published article URLs
   - Verify content displays correctly

2. ✅ **Add Feature Images**
   - Upload high-quality images
   - Add captions and alt text
   - Set as featured images

3. ✅ **Add Internal Links**
   - Link to related GigaNectar content
   - Use contextually relevant links
   - Improve site SEO structure

4. ✅ **Add External Links**
   - Link to primary sources
   - Add credibility with backlinks
   - Improve E-E-A-T signals

5. ✅ **Promote Articles**
   - Share on social media
   - Add to email newsletter
   - Cross-promote within site
   - Monitor engagement metrics

6. ✅ **Monitor Performance**
   - Track organic traffic
   - Monitor keyword rankings
   - Respond to comments
   - Update with new information

---

## Questions?

Refer to:
- `PUBLICATION-GUIDE.md` - Detailed publication overview
- `ARTICLES-SUMMARY.txt` - Complete article summary
- This file - Step-by-step instructions

**Ready to publish? Choose your method above and proceed!**

---

Generated: July 24, 2026  
Branch: claude/tech-news-publication-sogbvi
