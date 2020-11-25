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
       paddingVertical: 40,
       display: "flex",
       justifyContent: "center",
       width: "100%",
       borderBottomWidth: 1,
       borderBottomColor: 'red'
   },
   text: {
       fontWeight: "600",
       fontSize: 18,
       textAlign: "center"
   }
});