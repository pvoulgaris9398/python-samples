var dagcomponentfuncs  = (window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions ||{});

dagcomponentfuncs.ButtonHeader = function (props) {
    return React.createElement(
        'button',
        {
            id: props.id || 'button-header',
            onClick: () => {
                newData = {
                    id: props.id,
                    name: "peter",
                    valuable: true,
                    timestamp: new Date().toISOString(),
                    field: props.column?.colId
                }
                dash_clientside.set_props("store-button", {data:newData})
            },
            className: props.className,
            style: {
                backgroundColor: 'transparent',
                border: 'none',
                cursor: 'pointer',
                padding: '5px 10 px',
                color: 'inherit',
                font: 'inherit',
                ...props.style
            },
        },
        props.displayName)
};

dagcomponentfuncs.HeaderClickable = function (props){
    const onClick = () => {
        if (props.enableCallback){
            props.setValue({
               headerClicked: props.displayName,
               timestamp: new Date().toISOString() 
            });
        }
    }
    return React.createElement(
        'div',
        {
            onClick:onClick,
            style: {cursor: 'pointer', padding: '10px'}
        },
        props.displayName
    );
};

