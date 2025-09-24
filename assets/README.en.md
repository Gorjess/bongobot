# Created by 954860224@qq.com
# Assets Directory

This directory contains resource files required for BongoCat program operation.

**Language**: [🇺🇸 English](README.en.md) | [🇨🇳 中文](README.md)

## 📁 File Descriptions

### Template Image Files

- `test_btn.png` - Default test button template image
- `__test_btn.png` - Backup test button template image

These images are used for the program's image recognition feature. The program searches for areas on screen that match these templates and performs click operations.

## 🎯 How to Use

### 1. Using Default Templates
The program's default configuration already points to `assets/test_btn.png` and can be used directly.

### 2. Adding Custom Templates
1. Use screenshot tool to capture the target button you want to click
2. Save the image to this directory
3. Update the `template_path` configuration in `config.yaml`

### 3. Template Creation Best Practices
- **Format**: Recommend PNG format for transparency and clarity
- **Size**: Capture minimum recognition area, typically 50x50 to 200x200 pixels
- **Content**: Include characteristic parts of button, avoid changing text or numbers
- **Background**: Try to avoid complex backgrounds

## 📝 Configuration Example

Configure template path in `config.yaml`:

```yaml
clicker:
  enabled: true
  template_path: "assets/your_button.png"  # Point to your template file
  confidence: 0.8
```

## ⚠️ Important Notes

1. **File Paths**: Paths in configuration are relative to project root directory
2. **File Permissions**: Ensure program has read access to these files
3. **File Integrity**: Don't delete or move template files that are in use
4. **Version Control**: Consider adding personal custom template files to `.gitignore`

## 🛠️ Template Testing

To test your template effectiveness:

1. **Adjust Confidence**: Start with 0.8, adjust based on results
2. **Test Environment**: Test in the same environment where you'll use it
3. **Multiple Variations**: Create templates for different states (hover, pressed, etc.)
4. **Debug Mode**: Enable debug logging to see matching details

## 📋 Supported Formats

- **PNG** (Recommended): Best for transparency and precision
- **JPG/JPEG**: Good for photographs, but no transparency
- **BMP**: Basic format, larger file sizes

## 🎨 Template Quality Tips

### Good Templates
- Clear, distinctive features
- Consistent appearance across different times
- Minimal background elements
- High contrast with surroundings

### Avoid
- Templates with changing text/numbers
- Too much surrounding context
- Low contrast or blurry images
- Very small details that might not scale well

## 🔍 Troubleshooting

### Template Not Found
- Check file path in configuration
- Verify file exists and is readable
- Ensure correct file extension

### Poor Matching
- Adjust confidence value (0.7-0.9 range)
- Try different template cropping
- Check for screen scaling issues
- Verify target is visible and not obscured

### Performance Issues
- Use smaller template images when possible
- Avoid overly complex templates
- Consider reducing search frequency

---

For more detailed usage instructions, see [Usage Guide](../docs/en/usage.md).
