import React from 'react'
import {View, StyleSheet, Text} from "react-native";

export default function({title}) {
    return (
        <View style={styles.root}>
            <Text style={styles.text}>
                {title}
            </Text>
        </View>
    )
}

const styles = StyleSheet.create({
   root: {
       paddingTop: 60,
       paddingBottom: 30,
       display: "flex",
       justifyContent: "center",
       width: "100%",
   },
   text: {
       fontWeight: "700",
       fontSize: 22,
       textAlign: "center"
   }
});