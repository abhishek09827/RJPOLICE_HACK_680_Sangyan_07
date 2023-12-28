import 'package:flutter/material.dart';

class LandingPage extends StatelessWidget {
  const LandingPage({Key? key}) : super(key: key);


  @override
  Widget build(BuildContext context) {
    Image img = Image.network("https://cdn.leonardo.ai/users/60b506ce-f33e-4b59-8bad-2e3de2c14ab2/generations/f67a7c18-9819-40f3-a850-82eb148aed57/DreamShaper_v7_landing_page_image_for_financial_fraud_detectio_1.jpg?w=512");

    return Scaffold(
      body: Column(
        children: [
          Container(
            width: double.infinity,
            decoration: BoxDecoration(
              image: DecorationImage(
                  fit: BoxFit.fill,
                image: img.image
              )
            ),
          ),
          Container()
        ],
      ),
    );
  }
}
